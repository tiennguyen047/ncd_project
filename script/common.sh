#!/bin/bash
proj_repo="$(git rev-parse --show-toplevel)"
docker_file=${proj_repo}
image_name="ncd_image"
version="ncd_v_1"
packages=${proj_repo}/packages
path_docker_images=${proj_repo}/packages/${image_name}_${version}.tar
container_name="ncd_server"
port_publish_host="2345"
port_inside_docker_private="8080"
host_ip="192.168.2.25"