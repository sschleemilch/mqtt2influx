#!/bin/bash
SCRIPT_DIR=$(cd $(dirname "${BASH_SOURCE[0]}") && pwd)

SERVICE_FILE=/usr/lib/systemd/system/mqtt2influx.service
CONFIG_FILE=${SCRIPT_DIR}/config.yaml