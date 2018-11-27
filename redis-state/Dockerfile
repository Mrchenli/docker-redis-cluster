FROM ruby:2.4-alpine3.8

RUN gem sources --add https://gems.ruby-china.com/ --remove https://rubygems.org/

RUN gem install redis-stat

ADD requirements.txt /etc/redis/

RUN apk update && \
    apk add python3 && \
    pip3 install -r /etc/redis/requirements.txt

COPY wrapper.py /

ENTRYPOINT ["python3","/wrapper.py"]
