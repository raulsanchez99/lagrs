FROM ubuntu:22.04
RUN apt-get update && apt-get upgrade -y && \
apt-get install -y iputils-ping && \
apt-get install -y net-tools && \
apt-get install -y openssh-server && \
apt-get install -y openssh-client
RUN service ssh start
COPY entrypoint.sh /
COPY delta_hosts /tmp
ENTRYPOINT ["/entrypoint.sh"]
