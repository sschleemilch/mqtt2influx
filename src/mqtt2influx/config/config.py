from dataclasses import dataclass
from functools import cache
from typing import List, Optional, Tuple

from .device import Device
from .influx import Influx
from .mqtt_broker import MQTTBroker
from .topic import Topic


@dataclass
class Config:
    mqtt: MQTTBroker
    influx: Influx
    devices: List[Device]

    @cache
    def get_device_topic(self, search_topic: str) -> Optional[Tuple[Device, Topic]]:
        for device in self.devices:
            for topic in device.topics:
                if topic.name == search_topic:
                    return device, topic
        return None

    def __hash__(self) -> int:
        h = hash(self.mqtt) + hash(self.influx)
        for device in self.devices:
            h += hash(device)
        return h
