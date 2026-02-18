FROM ubuntu:22.04
RUN apt-get update && \
apt-get upgrade -y && \
apt-get install -y net-tools && \
apt-get install -y iputils-ping && \
apt-get install -y openssh-server && \
apt-get install -y locales && \
localedef -i es_ES -c -f UTF-8 -A /usr/share/locale/locale.alias es_ES.UTF-8
RUN mkdir /var/run/sshd
ENV LANG es_ES.UTF-8
COPY entrypoint.sh /
EXPOSE 22
ENTRYPOINT ["/entrypoint.sh"]
