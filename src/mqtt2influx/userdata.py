from influxdb_client import InfluxDBClient, WriteApi
from influxdb_client.client.write_api import SYNCHRONOUS

from .config.config import Config

class Userdata:
    def __init__(self, config: Config) -> None:
        self.config = config
        client = InfluxDBClient(url=f"{config.influx.url}:{config.influx.port}",
                                token=config.influx.token, org=config.influx.org)
        self.influx: WriteApi = client.write_api(write_options=SYNCHRONOUS)
