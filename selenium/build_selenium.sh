#!/bin/bash

proj_repo="$(git rev-parse --show-toplevel)"
jenkin_port=9812
jenkin_port_2=50000
port_inside_docker_private=9913
port_publish_host=9914
image_name="selenium_nqt"
version="se_v1.0"
BASE_OS="ubuntu"
BASE_OS_VERSION="22.04"
WORK_DIR="/usr/local/share"
container_name="nqt_selenium_service"

function f_build_selenium_images() {
    echo ${proj_repo}
    echo ${image_name}:${version}
    echo "port_inside_docker_private ${port_inside_docker_private}"
    echo "port_publish_host ${port_publish_host}"
    echo "remove images ${image_name}:${version}"
    docker rmi -f ${image_name}:${version}
    docker build -t ${image_name}:${version} \
        --build-arg OS_NAME=${BASE_OS} \
        --build-arg OS_VERSION=${BASE_OS_VERSION} \
        --build-arg W_DIR=${WORK_DIR} \
        "${proj_repo}/selenium/"
}

Help()
{
   # Display Help
   echo "Add description of the script functions here."
   echo "For build selenium images"
   echo "Syntax: scriptTemplate [-h|b]"
   echo "options:"
   echo "h     Print this Help."
   echo "b     build selenium images"
   echo "d     deploy selenium service"
   echo
}

function f_deploy_selenium() {
    local $IMAGE_NAME
    IMAGE_NAME=${image_name}:${version}
    if docker image inspect ${IMAGE_NAME} >/dev/null 2>&1; then
        echo "Deployment ${IMAGE_NAME}"
        docker run -d -itd --network host --name ${container_name} ${IMAGE_NAME}
    else
        echo "Image does not exist locally"
        echo "build images ${image_name}:${version}"
        f_build_selenium_images
    fi
}


while getopts ":h,b,d" option; do
   case $option in
        h) # display Help
            Help
            exit;;
        b)
            f_build_selenium_images 2>&1 | tee -a build_selenium.log
            exit;;
        d)
            f_deploy_selenium 2>&1 | tee -a deploy_selenium.log
            exit;;
   esac
done