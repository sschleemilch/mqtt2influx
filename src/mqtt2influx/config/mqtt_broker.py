from dataclasses import dataclass

@dataclass
class MQTTBroker:
    url: str
    port: int

    def __repr__(self) -> str:
        return f"MQTTBroker, {self.url=}, {self.port=}"

    def __hash__(self) -> int:
        return hash(self.url) + hash(self.port)