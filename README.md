# docker-redis-cluster
```json
关键字:
  docker-swarm 
  redis-cluster 
  zookeeper 
  redis-state  
```

```json
环境变量
  redis:
    ZK_HOSTS
    BIND_IP / NET_IFACE (127.0.0.1 / eth0)
    PORT
  
  redis-stat:
    ZK_HOSTS
    PORT
```

```json
问题：
1.动态ip问题 怎么解决
2.跨主机的volume + slot 可以解决数据存储的问题
```
