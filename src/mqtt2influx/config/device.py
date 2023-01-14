from dataclasses import dataclass
from typing import List, Dict
from .topic import Topic

@dataclass
class Device:
    name: str
    topics: List[Topic]
    location: str
    tags: Dict[str, str]
    group: str

    def __repr__(self) -> str:
        return f"Device, {self.name=}, {self.location=}, {self.tags=}, {self.topics=}, {self.group=}"

    def __hash__(self) -> int:
        h = hash(self.name) + hash(self.location) + hash(self.group)
        for key, value in self.tags.items():
            h += hash(key) + hash(value)
        for topic in self.topics:
            h += hash(topic)
        return h