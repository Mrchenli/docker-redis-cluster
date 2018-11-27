from kazoo.client import KazooClient
import os, time, shlex, subprocess, sys

zk_hosts = os.environ.get("ZK_HOSTS") or '127.0.0.1:2181'
bind_ip = os.environ.get("BIND_IP") or '127.0.0.1'  # add by kiibos
interface = os.environ.get("NET_IFACE") or 'eth0'
port = os.environ.get("PORT") or "63790"

# uid = str(uuid.uuid4())
is_master = False

zk = KazooClient(hosts=zk_hosts)
redis_nodes = '/redis/nodes'
redis_cluster = '/redis/cluster'


def get_cluster_cmd(cluster_url):
    c = "echo yes | redis-cli --cluster create --cluster-replicas 1 {}".format(cluster_url)
    return c
    #return shlex.split(c)


def get_redis_live_url(children):
    redis_live_url = ""
    for i in children:
        tmp_key = redis_nodes + "/" + i
        tmp_value = zk.get(tmp_key)[0] + b' '
        redis_live_url += tmp_value.decode("utf-8")
    return redis_live_url


# waiting for impl
def re_sharding_nodes():
    print("re-sharding-nodes")


# waiting for impl
def start_redis_stat(redis_live_url):
    c = "redis-stat {} --server={} 5 --daemon".format(redis_live_url, port)
    print("redist-stat starting ... {}".format(c))
    subprocess.run(c, shell=True)


@zk.ChildrenWatch('/redis/nodes')
def watch_children(children):
    with zk.Lock('/redis/master', "master-update") as lock:
        # 先获取cluster信息 如果是第一次cluster
        redis_cluster_url = zk.get(redis_cluster)[0]
        redis_live_url = get_redis_live_url(children)
        print("========>redis_cluster_url is {}".format(redis_cluster_url))
        print("========>redis_live_url is {}".format(redis_live_url))
        if redis_cluster_url == b'':
            print("initializing cluster...")
            cmd = get_cluster_cmd(redis_live_url)
            subprocess.run(cmd, shell=True)
            zk.set(redis_cluster, str.encode(redis_live_url))
            start_redis_stat(redis_live_url)
        else:
            died_nodes = []
            new_nodes = []
            re_sharding_nodes()


def setup_zk():
    assert zk.connected
    zk.ensure_path(redis_cluster)


zk.start()
setup_zk()

while True:
    time.sleep(10)
    print("ok")
