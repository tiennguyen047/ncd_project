#!/bin/bash

# shellcheck disable=SC2034
proj_repo="$(git rev-parse --show-toplevel)"
CWD=$(pwd)
version="v1.7.1"
IMAGE_NAME="availj/avail:${version}"
echo "${IMAGE_NAME}"
node_name="vail_nqt_node"
# docker run -v $HOME/avail-node/data/state:/da/state:rw -v $HOME/avail-node/data/keystore:/da/keystore:rw -e DA_CHAIN=goldberg -e DA_NAME=goldberg-docker-avail-Node -p 0.0.0.0:30333:30333 -p 9615:9615 -p 9944:9944 -d --restart unless-stopped availj/avail:v1.8.0.0





f_config_avail() {
    mkdir -p "${CWD}"/avail-node/data/keystore
    mkdir -p "${CWD}"/avail-node/data/state
    if docker image inspect ${IMAGE_NAME} >/dev/null 2>&1; then
        echo "Image ${IMAGE_NAME} exists locally"
    else
        echo "Image ${IMAGE_NAME} does not exist locally"
        docker pull ${IMAGE_NAME}
    fi
}

f_deploy_node() {
    # docker run -v "${CWD}"/avail-node/data/state:/da/state:rw -v "${CWD}"/avail-node/data/keystore:/da/keystore:rw \
    # -e DA_CHAIN=goldberg \
    # -e DA_NAME=${node_name} \
    # -p 0.0.0.0:30333:30333 \
    # -p 9615:9615 \
    # -p 9944:9944 \
    # -d --restart unless-stopped ${IMAGE_NAME}

    # cd /mnt/avail || exit
    # # shellcheck disable=SC2046
    # docker run -v $(pwd)/state:/da/state:rw \
    # -p 30333:30333 \
    # -p 9615:9615 \
    # -p 9944:9944 -d --restart unless-stopped availj/avail:v1.8.0.4 \
    # --chain goldberg --name "MyAweasomeInContainerAvailAnode" \
    # -d /da/state

    docker run -v "${CWD}"/avail-node/data/state:/da/state:rw \
    -p 30333:30333 \
    -p 9615:9615 \
    -p 9944:9944 \
    -d --restart unless-stopped availj/avail:v1.8.0.4 --chain goldberg --name "nqt-node-test" -d avail-node/data/da/state

}

f_random() {
    random_string=$(cat /dev/urandom | tr -dc 'a-zA-Z0-9' | fold -w 10 | head -n 1)
}



f_deploy_2_node() {
    f_random
    mount_dir="${CWD}"/data_node/state
    echo "${mount_dir}"
    mkdir -p "${mount_dir}"
    images_name="availj/avail:v1.8.0.4"
    chain_name="goldberg"
    node_name="nqt_"

    docker run -v "${CWD}"/data_node/state:/da/state:rw \
    -p 30333:30333 \
    -p 9615:9615 \
    -p 9944:9944 \
    -d --restart unless-stopped availj/avail:v1.8.0.4 --chain goldberg --name "nqt-node-test" -d avail-node/data/da/state
}

f_get_log_node() {
    f_random
}


f_deploy_angiang_node() {
    local name="an_giang"
    local cwd=$(pwd)
    local mount_data="data_node_${name}"
    local mount_dir="${cwd}"/${mount_data}/state
    echo "${mount_dir}"
    mkdir -p "${mount_dir}"
    local images_name="availj/avail:v1.8.0.5"
    local chain_name="goldberg"
    local node_name="avail_node_${name}"

    docker run -v "${CWD}"/${mount_data}/state:/da/state:rw \
    -p 30334:30333 \
    -p 9616:9615 \
    -p 9945:9944 \
    -d --restart unless-stopped "${images_name}" --chain "${chain_name}" --name "${node_name}" -d /da/state
}


#######################################################################################
#
# Main function
#
#######################################################################################

# while getopts ":h" opt; do

#     # shellcheck disable=SC2220
#     # shellcheck disable=SC2214
#     case "${opt}" in
#         h)
#             echo "help"
#         ;;
#         *)
#             echo "help"
#         ;;
#     esac
# done
# f_random
# f_config_avail
f_deploy_2_node