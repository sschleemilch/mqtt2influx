#!/bin/bash
SCRIPT_DIR=$(cd $(dirname "${BASH_SOURCE[0]}") && pwd)

DIST_DIR=${SCRIPT_DIR}/dist

if [ -d "$DIST_DIR" ] ;
  then rm -rf $DIST_DIR
fi

poetry build --format wheel --directory $SCRIPT_DIR

echo "Copying scripts"
cp ${SCRIPT_DIR}/scripts/*.sh $DIST_DIR

echo "Copying reference config"
cp ${SCRIPT_DIR}/docs/reference.yaml ${DIST_DIR}/config.yaml

echo "Creating tar.gz"
tar -czf mqtt2influx-${1}.tar.gz -C ${DIST_DIR} .