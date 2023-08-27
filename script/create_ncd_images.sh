#!/bin/bash
source "$(realpath $(dirname $0))"/common.sh
SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )

###################################################################
#FUNCTION
#
###################################################################

function f_print_Params() {

    echo "path of create_ncd_image.sh is:   ${SCRIPT_DIR}"
    echo "git dir:                          ${proj_repo}"
    # echo "NQT"
}

function f_printUsage() {
    echo Usage:
    echo "-b build with tag. Default:  ${SCRIPT_DIR} "
    echo "-h help "
}

function f_save_docker_image() {
    echo "save docker images at ${path_docker_images}"
    docker save -o ${path_docker_images} ${image_name}:${version}

}

function f_build_docker_images() {
    echo ${proj_repo}
    echo ${image_name}:${version}
    echo "port_inside_docker_private ${port_inside_docker_private}"
    echo "port_publish_host ${port_publish_host}"
    # docker build --no-cache -t ${image_name}:${version} ${proj_repo}
    docker build -t ${image_name}:${version} \
        --build-arg COMMON_PATH=${NCD_COMMON_PATH} \
        --build-arg OS_NAME=${BASE_OS} \
        --build-arg OS_VERSION=${BASE_OS_VERSION} \
        --build-arg PORT_PRIVATE=${port_inside_docker_private} \
        --build-arg PORT_EXPOSE=${port_publish_host} \
        --build-arg PY_SITE_PACKAGES=${pip_site_package} \
        ${proj_repo}
}

function f_remove_image_tar() {
    echo "nqt"
    echo "remove ${path_docker_images}"
    echo ${packages}
    rm -rf ${packages}
    mkdir ${packages}
}

###################################################################
#Main function
#
###################################################################

f_print_Params
f_printUsage
f_remove_image_tar
f_build_docker_images
f_save_docker_image