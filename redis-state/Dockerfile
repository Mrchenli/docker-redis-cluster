FROM ruby:2.4-alpine3.8

RUN apk update && \
    apk add python3 && \
    apk add build-essential && \
    pip3 install -r /etc/redis/requirements.txt

RUN gem install redis-stat

ADD requirements.txt /etc/redis/

COPY wrapper.py /

ENTRYPOINT ["python3","/wrapper.py"]
