#!/bin/bash

# shellcheck disable=SC2034
# proj_repo="$(git rev-parse --show-toplevel)"
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
    local cwd=$(pwd)
    mount_dir="${cwd}"/data_node/state
    echo "${mount_dir}"
    mkdir -p "${mount_dir}"
    images_name="availj/avail:v1.8.0.5"
    chain_name="goldberg"
    node_name="avail_node_binhduong"

    docker run -v "${CWD}"/data_node/state:/da/state:rw \
    -p 30333:30333 \
    -p 9615:9615 \
    -p 9944:9944 \
    -d --restart unless-stopped availj/avail:v1.8.0.5 --chain goldberg --name "avail_node_binhduong" -d /da/state
}

f_deploy_haiphong_node() {
    local cwd=$(pwd)
    local mount_data="data_node_haiphong"
    local mount_dir="${cwd}"/${mount_data}/state
    echo "${mount_dir}"
    mkdir -p "${mount_dir}"
    local images_name="availj/avail:v1.8.0.5"
    local chain_name="goldberg"
    local node_name="avail_node_haiphong"

    docker run -v "${CWD}"/${mount_data}/state:/da/state:rw \
    -p 30334:30333 \
    -p 9616:9615 \
    -p 9945:9944 \
    -d --restart unless-stopped "${images_name}" --chain "${chain_name}" --name "${node_name}" -d /da/state
}

f_deploy_binhphuoc_node() {
    local cwd=$(pwd)
    local mount_data="data_node_binhphuoc"
    local mount_dir="${cwd}"/${mount_data}/state
    echo "${mount_dir}"
    mkdir -p "${mount_dir}"
    local images_name="availj/avail:v1.8.0.5"
    local chain_name="goldberg"
    local node_name="avail_node_binhphuoc"

    docker run -v "${cwd}"/${mount_data}/state:/da/state:rw \
    -p 30335:30333 \
    -p 9617:9615 \
    -p 9946:9944 \
    -d --restart unless-stopped "${images_name}" --chain "${chain_name}" --name "${node_name}" -d /da/state
}

f_deploy_hue_node() {
    local cwd=$(pwd)
    local mount_data="data_node_hue"
    local mount_dir="${cwd}"/${mount_data}/state
    echo "${mount_dir}"
    mkdir -p "${mount_dir}"
    local images_name="availj/avail:v1.8.0.5"
    local chain_name="goldberg"
    local node_name="avail_node_hue"

    docker run -v "${cwd}"/${mount_data}/state:/da/state:rw \
    -p 30336:30333 \
    -p 9618:9615 \
    -p 9947:9944 \
    -d --restart unless-stopped "${images_name}" --chain "${chain_name}" --name "${node_name}" -d /da/state
}

f_deploy_hochiminh_node() {
    local cwd=$(pwd)
    local mount_data="data_node_hochiminh"
    local mount_dir="${cwd}"/${mount_data}/state
    mkdir -p "${mount_dir}"
    local images_name="availj/avail:v1.8.0.5"
    local chain_name="goldberg"
    local node_name="avail_node_hochiminh"

    docker run -v "${cwd}"/${mount_data}/state:/da/state:rw \
    -p 30337:30333 \
    -p 9619:9615 \
    -p 9948:9944 \
    -d --restart unless-stopped "${images_name}" --chain "${chain_name}" --name "${node_name}" -d /da/state
}

f_get_log_node_hochiminh() {
    echo "************************************" 2>&1 | tee -a avail_node_hochiminh.log
    echo "************************************" 2>&1 | tee -a avail_node_hochiminh.log
    echo "************************************" 2>&1 | tee -a avail_node_hochiminh.log
    docker logs gifted_wright 2>&1 | tee -a avail_node_hochiminh.log
}

f_get_log_node_binhduong() {
    echo "************************************" 2>&1 | tee -a avail_node_binhduong.log
    echo "************************************" 2>&1 | tee -a avail_node_binhduong.log
    echo "************************************" 2>&1 | tee -a avail_node_binhduong.log
    docker logs hungry_lederberg 2>&1 | tee -a avail_node_binhduong.log
}

f_get_log_node_haiphong() {
    echo "************************************" 2>&1 | tee -a avail_node_haiphong.log
    echo "************************************" 2>&1 | tee -a avail_node_haiphong.log
    echo "************************************" 2>&1 | tee -a avail_node_haiphong.log
    docker logs stupefied_wilbur 2>&1 | tee -a avail_node_haiphong.log
}

f_get_log_node_hue() {
    echo "************************************" 2>&1 | tee -a avail_node_hue.log
    echo "************************************" 2>&1 | tee -a avail_node_hue.log
    echo "************************************" 2>&1 | tee -a avail_node_hue.log
    docker logs awesome_hertz 2>&1 | tee -a avail_node_hue.log
}

f_get_session_keys_hue() {
    local container_id_hue="f9874cdc4846"
    docker exec -i "${container_id_hue}" curl -sH "Content-Type: application/json" -d '{"id":1, "jsonrpc":"2.0", "method": "author_rotateKeys", "params":[]}' http://localhost:9944 2>&1 | tee -a session_keyhue.log
}

f_get_session_keys_binhduong() {
    local container_id_binhduong="3fd6e49dd384"
    docker exec -i "${container_id_binhduong}" curl -sH "Content-Type: application/json" -d '{"id":1, "jsonrpc":"2.0", "method": "author_rotateKeys", "params":[]}' http://localhost:9944 2>&1 | tee -a session_key_binhduong.log
}

#######################################################################################
#
# Main function
#
#######################################################################################

# f_random
# f_config_avail
# f_deploy_haiphong_node
# f_deploy_binhphuoc_node
# f_deploy_hue_node
# f_deploy_2_node
# f_get_log_node_binhduong
# f_get_log_node_haiphong
# f_deploy_hochiminh_node
# f_get_log_node_hue

# f_get_session_keys_hue
f_get_session_keys_binhduong

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
