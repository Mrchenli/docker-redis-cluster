FROM redis:5-alpine

ADD requirements.txt /etc/redis/

RUN apk update && \
    apk add build-base && \
    apk add python3 && \
    pip3 install -r /etc/redis/requirements.txt


RUN apk update \
&& apk add ruby \
           ruby-bigdecimal \
           ruby-bundler \
           ruby-io-console \
           ruby-irb \
           ca-certificates \
           libressl \
           less \
&& apk add --virtual build-dependencies \
           build-base \
           ruby-dev \
           libressl-dev \
\
&& bundle config build.nokogiri --use-system-libraries \
&& bundle config git.allow_insecure true \
&& gem install json \
&& gem install rdoc \
&& gem install redis-stat \
\
&& gem cleanup \
&& apk del build-dependencies \
&& rm -rf /usr/lib/ruby/gems/*/cache/* \
          /var/cache/apk/* \
          /tmp/* \
          /var/tmp/*


COPY wrapper.py /

ENTRYPOINT ["python3","/wrapper.py"]
