FROM ruby:2.4-alpine3.8


ADD requirements.txt /etc/redis/

RUN apk update && \
    apk add build-base && \
    apk add python3 && \
    pip3 install -r /etc/redis/requirements.txt

RUN gem install redis-stat


COPY wrapper.py /

ENTRYPOINT ["python3","/wrapper.py"]
