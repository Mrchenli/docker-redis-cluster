FROM redis:5-alpine

ADD requirements.txt /etc/redis/

RUN apk update && \
    apk add build-base && \
    apk add ruby && \
    apk add ruby-dev  && \
    apk add python3 && \
    pip3 install -r /etc/redis/requirements.txt


RUN gem install rdoc
RUN gem install redis-stat


COPY wrapper.py /

ENTRYPOINT ["python3","/wrapper.py"]
