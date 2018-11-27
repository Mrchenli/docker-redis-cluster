#!/bin/bash

docker network create --driver overlay --subnet 10.0.10.0/24 redis-cluster