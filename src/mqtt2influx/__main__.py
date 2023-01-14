import logging
import time
from pathlib import Path

import rich_click as click
from rich.logging import RichHandler
from rich.traceback import install
import paho.mqtt.client as mqtt
from influxdb_client import Point

from . import __version__
from . import constants as c
from .config.loader import load
from .config.config import Config
from .config.device import Device
from .config.topic import Topic
from .userdata import Userdata

FORMAT = "%(message)s"
logging.basicConfig(
    level="INFO", 
    format=FORMAT, 
    datefmt="[%X]", 
    handlers=[RichHandler(rich_tracebacks=True)]
)

logger = logging.getLogger(c.LOGGER_NAME)

def configure_run_mode(verbose: int) -> None:
    if verbose > 2:
        logger.setLevel("DEBUG")
        install(show_locals=True)
    elif verbose > 1:
        logger.setLevel("INFO")
    elif verbose > 0:
        logger.setLevel("WARNING")
    else:
        logger.setLevel("ERROR")

def mqtt_subscribe(client, config: Config):
    logger.info("Subscribing to device topics")
    for device in config.devices:
        for topic in device.topics:
            logger.debug(f"Subscribing to {topic}")
            client.subscribe(topic.name)

def mqtt_on_connect(client, userdata: Userdata, flags, rc):
    logger.info("MQTT connect")
    if rc == 0:
        logger.info(f"Successfully connected to {userdata.config.mqtt}")
        mqtt_subscribe(client, userdata.config)
    else:
        logger.error(f"Could not connect to {userdata.config.mqtt}")

def get_influx_point(device: Device, topic: Topic, value: float) -> Point:
    point = Point(device.group).time(int(round(time.time() * 1000000000)))
    point.tag("location", device.location)
    for tag_key, tag_value in device.tags.items():
        point.tag(tag_key, tag_value)
    point.field(topic.type, value)
    return point

def mqtt_on_message(client, userdata: Userdata, msg):
    payload = round(float(msg.payload.decode('utf-8')), 1)
    logger.info(f"Got MQTT Message, topic '{msg.topic}', payload: '{payload}'")
    device, topic = userdata.config.get_device_topic(msg.topic)
    point = get_influx_point(device, topic, payload)
    logger.debug(f"Writing point: {point}")
    userdata.influx.write(userdata.config.influx.bucket, userdata.config.influx.org, record=point)

def mqtt_loop(userdata: Userdata):
    client = mqtt.Client(userdata=userdata)
    client.on_connect = mqtt_on_connect
    client.on_message = mqtt_on_message
    logger.info(f"Connecting to '{userdata.config.mqtt}'")
    client.connect(userdata.config.mqtt.url, userdata.config.mqtt.port)
    client.loop_forever()

@click.command()
@click.version_option(__version__)
@click.option("-v", "--verbose", count=True, help="Verbositiy level, can be given up to 3 times (-vvv)")
@click.option(
    "-c",
    "--config",
    required=True,
    type=click.Path(exists=True, dir_okay=False, readable=True, path_type=Path),
    help="YAML config file.",
)
def main(
    verbose: int,
    config: Path):

    configure_run_mode(verbose)
    userdata = Userdata(load(config_path=config))
    mqtt_loop(userdata)

if __name__ == "__main__":
    main()
