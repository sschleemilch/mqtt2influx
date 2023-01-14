#!/bin/bash

SCRIPT_DIR=$(cd $(dirname "${BASH_SOURCE[0]}") && pwd)

source ${SCRIPT_DIR}/config.sh

echo "Creating venv in $SCRIPT_DIR"
python -m venv ${SCRIPT_DIR}/env

echo "Activating venv"
. ${SCRIPT_DIR}/env/bin/activate

echo "Installing wheel"
pip install *.whl

START_SCRIPT=${SCRIPT_DIR}/start.sh


echo "Creating service file ${SERVICE_FILE}"
cat >${SERVICE_FILE} <<EOF
[Unit]
Description=MQTT to InfluxDB Aggregator
After=network-online.target

[Service]
ExecStart=/bin/bash ${START_SCRIPT}
WorkingDirectory=${SCRIPT_DIR}
StandardOutput=inherit
StandardError=inherit
Restart=always

[Install]
WantedBy=multi-user.target
EOF

echo "Installation finished. You can start or enable the service with sudo systemctl enable/start mqtt2influx.service"