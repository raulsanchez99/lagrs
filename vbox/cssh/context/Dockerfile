FROM ubuntu:22.04
RUN apt-get update && apt-get upgrade -y && \
apt-get install -y locales && \
localedef -i es_ES -c -f UTF-8 \
-A /usr/share/locale/locale.alias es_ES.UTF-8
RUN apt-get update && apt-get upgrade -y && \
apt-get install -y sudo && \
apt-get install -y openssh-server && \
apt-get install -y openssh-client && \
sudo apt-get install -y sshfs
RUN useradd -rm -d /home/raulsm -s /bin/bash -u 1001 raulsm
RUN service ssh start
ENV LANG es_ES.UTF-8
COPY entrypoint.sh /
ENTRYPOINT ["/entrypoint.sh"]

