FROM ubuntu:24.04
RUN apt-get update && apt-get upgrade -y && apt-get install -y sysvbanner
COPY entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]
RUN useradd -rm -d /home/raulsm -s /bin/bash -u 1000 raulsm
USER raulsm
WORKDIR /home/raulsm
