FROM ruby:2.4

RUN gem install redis-stat

COPY wrapper.py /

ENTRYPOINT ["python3","/wrapper.py"]
