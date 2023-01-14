from dataclasses import dataclass

@dataclass
class Influx:
    url: str
    port: int
    token: str
    org: str
    bucket: str

    def __repr__(self) -> str:
        return f"InfluxDB Config, {self.url=}, {self.port=}, {self.org=}, {self.bucket=}"

    def __hash__(self) -> int:
        return hash(self.url) + hash(self.port) + hash(self.token) + hash(self.org) + hash(self.bucket)