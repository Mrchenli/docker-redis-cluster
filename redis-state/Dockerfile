FROM ruby:2.4

RUN gem install redis-stat

ADD requirements.txt /etc/redis/

RUN apt-get update && \
    apt-get add python3 && \
    pip3 install -r /etc/redis/requirements.txt

COPY wrapper.py /

ENTRYPOINT ["python3","/wrapper.py"]
