from kazoo.client import KazooClient
import os, shlex, subprocess, socket, fcntl, struct

zk_hosts = os.environ.get("ZK_HOSTS") or '127.0.0.1:2181'
bind_ip = os.environ.get("BIND_IP")
interface = os.environ.get("NET_IFACE") or 'eth0'
port = os.environ.get("PORT") or "7000"

# uid = str(uuid.uuid4())
is_master = False

zk = KazooClient(hosts=zk_hosts)

redis_nodes = '/redis/nodes'


def setup_zk():
    assert zk.connected
    zk.ensure_path(redis_nodes)


def register():
    assert zk.connected
    ip_port_key = "{}:{}".format(get_ip_address(interface),port)
    s = "{}:{}".format(get_ip_address(interface), port)
    tmp_path = redis_nodes+"/"+ip_port_key
    zk.create(tmp_path, bytes(s, encoding='UTF-8'), ephemeral=True)


def get_master_cmd():
    c = "redis-server /etc/redis/redis.conf --port {}".format(port)
    return shlex.split(c)


def get_ip_address(ifname):
    if bind_ip is not None:
        return bind_ip
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(
        s.fileno(),
        0x8915,  # SIOCGIFADDR
        struct.pack('256s', bytes(ifname, 'utf-8'))
    )[20:24])


zk.start()
setup_zk()
register()

cmd = get_master_cmd()


#zk.stop()

try:
    print("Running: " + str(cmd))
    subprocess.call(cmd)
    subprocess.run("tail -f /data/redis_7000.log", shell=True)
except:
    print("Exiting...")
