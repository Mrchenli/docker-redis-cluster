FROM redis:5-alpine

ADD requirements.txt /etc/redis/

RUN apk update && \
    apk add python3 && \
    pip3 install -r /etc/redis/requirements.txt
ADD redis.conf /etc/redis/
ADD wrapper.py /etc/redis/

ENTRYPOINT ["python3","/etc/redis/wrapper.py"]
