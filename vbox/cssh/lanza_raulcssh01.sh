#!/bin/bash
docker run --cap-add SYS_ADMIN --device /dev/fuse --security-opt apparmor:unconfined -it -h raulcssh01 --name raulcssh01 --rm raulsm/cssh
