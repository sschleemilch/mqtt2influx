import logging
from pathlib import Path
from typing import Any, Dict, List

import yaml

from .. import constants as c
from .config import Config
from .device import Device
from .influx import Influx
from .mqtt_broker import MQTTBroker
from .topic import Topic

logger = logging.getLogger(c.LOGGER_NAME)


def get_mqtt_broker(config: Dict[str, Any]) -> MQTTBroker:
    logger.debug("Creating mqtt broker config")
    broker = config.get("mqtt", {}).get("broker")
    url = broker.get("url")
    port = int(broker.get("port"))
    mqtt_broker = MQTTBroker(url=url, port=port)
    logger.debug(mqtt_broker)
    return mqtt_broker


def get_influx(config: Dict[str, Any]) -> Influx:
    logger.debug("Creating influxdb config")
    influx = config.get("influxdb", {})
    url = influx.get("url")
    port = int(influx.get("port"))
    token = influx.get("token")
    org = influx.get("org")
    bucket = influx.get("bucket")
    influx_config = Influx(url=url, port=port, token=token, org=org, bucket=bucket)
    logger.debug(influx_config)
    return influx_config


def get_devices(config: Dict[str, Any]) -> List[Device]:
    logger.debug("Creating devices config")
    devices: List[Device] = []
    for device in config.get("devices", []):
        name = device.get("name")
        location = device.get("location", "unknown")
        tags = device.get("tags")
        group = device.get("group", "default")
        topics: List[Topic] = []
        for topic in device.get("topics"):
            topics.append(Topic(name=topic.get("name"), type=topic.get("type")))
        devices.append(Device(name=name, location=location, tags=tags, topics=topics, group=group))
    logger.debug(devices)
    return devices


def load(config_path: Path) -> Config:
    logger.debug(f"Loading config: {config_path.absolute()}")
    with open(config_path, "r") as f:
        config = yaml.safe_load(f)
    mqtt_broker = get_mqtt_broker(config)
    influx = get_influx(config)
    devices = get_devices(config)
    return Config(mqtt=mqtt_broker, influx=influx, devices=devices)
