source "$(realpath $(dirname $0))"/common.sh
SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
PROJECT_REPO="$(git rev-parse --show-toplevel)"


function f_print_Params() {

    echo "path of build.bash is:    ${SCRIPT_DIR}"
    echo "git dir:                  ${PROJECT_REPO}"
    echo "NQT"
}

function f_printUsage() {
    echo Usage:
    echo "-b build with tag. Default:  ${SCRIPT_DIR} "
    echo "-h help "
}

function f_deployment() {
    echo "Start deployment service"
    echo "port inside docker private ${port_inside_docker_private}"
    echo "port publish local host ${port_publish_host}"
    docker run --name ${container_name} -p ${port_publish_host}:${port_inside_docker_private} ${image_name}:${version}

}

###################################################################
#Main function
#
###################################################################

f_print_Params
f_printUsage
f_deployment
