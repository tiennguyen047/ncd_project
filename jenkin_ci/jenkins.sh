#!/bin/bash
# docker pull jenkins/jenkins
# deploy with mount option, backup data in jenkins/home
# docker run -p 8080:8080 -p 50000:50000 -d -v jenkins_home:/var/jenkins_home jenkins/jenkins:latest
proj_repo="$(git rev-parse --show-toplevel)"
jenkin_port=9812
jenkin_port_2=50000
jenkin_images="jenkins_nqt:nqt_v111"
jenkin_container_name="jenkins_server-NQT"

jenkins_data="${proj_repo}/jenkin_ci/jenkins_data"
jenkins_docker_certs="${proj_repo}/jenkin_ci/jenkins_docker_certs"




function deploy_jenkin() {
    mkdir -p ${jenkins_data}
    mkdir -p ${jenkins_docker_certs}
    docker run --name ${jenkin_container_name} --restart=on-failure --detach \
    --network jenkins --env DOCKER_HOST=tcp://docker:2376 \
    --env DOCKER_CERT_PATH=/certs/client --env DOCKER_TLS_VERIFY=1 \
    --publish ${jenkin_port}:8080 --publish ${jenkin_port_2}:50000  \
    --volume ${jenkins_data}:/var/jenkins_home \
    --volume ${jenkins_docker_certs}:/certs/client:ro \
    docker:dind \
    ${jenkin_images}

}

function jenkins_network() {
    docker network create jenkins
}

function get_jenkin_pass() {
    cat ${jenkins_data}/secrets/initialAdminPassword
}

function build_jenkin_images() {
    mkdir -p archive
    docker build -t ${jenkin_images} jenkin_ci/
    docker save -o  archive/${jenkin_images}.tar ${jenkin_images}
}

function start_docker_dind() {
    docker run \
    --name jenkins-docker-dind \
    --rm \
    --detach \
    --privileged \
    --network jenkins \
    --network-alias docker \
    --env DOCKER_TLS_CERTDIR=/certs \
    --volume ${jenkins_docker_certs}:/certs/client \
    --volume ${jenkins_data}:/var/jenkins_home \
    --publish 2376:2376 \
    docker:dind \
    --storage-driver overlay2
}


Help()
{
   # Display Help
   echo "Add description of the script functions here."
   echo
   echo "Syntax: scriptTemplate [-b|h|d|p|s]"
   echo "options:"
   echo "d     start docker dind"
   echo "h     Print this Help."
   echo "b     build jenkin images"
   echo "V     Print software version and exit."
   echo
}

while getopts ":h,b,d,p,s" option; do
   case $option in
        h) # display Help
            Help
            exit;;
        b)
            build_jenkin_images
            exit;;
        d)
            start_docker_dind
            exit;;
        p)
            get_jenkin_pass
            exit;;
        s)
            deploy_jenkin
            exit;;
   esac
done
