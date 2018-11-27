FROM ruby:2.4

RUN gem install redis-stat

ENTRYPOINT ["python3","/etc/redis/wrapper.py"]
