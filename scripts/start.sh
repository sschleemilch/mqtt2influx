#!/bin/bash

SCRIPT_DIR=$(cd $(dirname "${BASH_SOURCE[0]}") && pwd)

source ${SCRIPT_DIR}/config.sh

. env/bin/activate

mqtt2influx --config ${CONFIG_FILE}