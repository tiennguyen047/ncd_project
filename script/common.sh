#!/bin/bash
# [default value]
proj_repo="$(git rev-parse --show-toplevel)"
docker_file=${proj_repo}
image_name="ncd_image"
version="ncd_v_1"
packages=${proj_repo}/packages
path_docker_images=${proj_repo}/packages/${image_name}_${version}.tar
container_name="ncd_server"
host_ip="10.0.2.15"

# [arg docker file]
NCD_COMMON_PATH=/usr/local/share
BASE_OS="ubuntu"
BASE_OS_VERSION="latest"
port_inside_docker_private=8080
port_publish_host=2345
myip="$(hostname -I | cut -d' ' -f1)"
myip_test="$(ifconfig | sed -En 's/127.0.0.1//;s/.*inet (addr:)?(([0-9]*\.){3}[0-9]*).*/\2/p')"
pip_site_package=${proj_repo}/build/package_requirements.txt


# For stock docker file,only get info about vntock technology


# for test, # TODO: need to remote
# for ip_host in ${myip_test}
# do
#     echo ${ip_host}
# done

# echo "********************"
# echo ${myip}
# echo "$(myip_test | cut -d' ' -f1)"