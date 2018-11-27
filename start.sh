#!/bin/bash

docker network create --driver overlay --subnet 10.0.10.0/24 redis-cluster


docker stack deploy -c docker-compose-zk.yml redis_cluster
echo "zk is up ... "
sleep 5s

docker stack deploy -c docker-compose-redis.yml redis_cluster
echo "redis is up ..."

sleep 10s


docker stack deploy -c docker-compose-redis-stat.yml redis_cluster
echo "redis-stat is up ..."