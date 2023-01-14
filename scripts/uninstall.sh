#!/bin/bash
SCRIPT_DIR=$(cd $(dirname "${BASH_SOURCE[0]}") && pwd)

source ${SCRIPT_DIR}/config.sh

systemctl stop mqtt2influx.service || echo "Service not running"

echo "Removing Service ${SERVICE_FILE}"
rm -rf ${SERVICE_FILE}