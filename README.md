# MQTT to InfluxDB Aggregator

`mqtt2influx` is an adapter to gather mqtt subscriptions and publish them to influxdb.

```
DEVICE 1 ---> +--------------+                      +----------+
DEVICE 2 ---> |  MQTT Broker | ---> mqtt2influx --> | InfluxDB |
DEVICE 3 ---> +--------------+                      +----------+
```

It is configurable through a [YAML configuration](docs/reference.yaml) file.

## Requrirements
- A running mqtt broker
- A running influx db
- Python 3.7+

## Contributing

See [here](CONTRIBUTING.md) if you would like to contribute. 
