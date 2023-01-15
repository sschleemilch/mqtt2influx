# MQTT to InfluxDB Aggregator

`mqtt2influx` is an adapter to gather mqtt subscriptions and publish them to influxdb.

```
DEVICE 1 -> +--------------+                   +----------+
DEVICE 2 -> |  MQTT Broker | -> mqtt2influx -> | InfluxDB |
DEVICE 3 -> +--------------+                   +----------+
```

It is configurable through a [YAML configuration](docs/reference.yaml) file.

## Requirements
- A running mqtt broker (e.g. [mosquitto](https://mosquitto.org/)) somewhere, for instance on a Raspberry Pi
- A running [influx db](https://www.influxdata.com/) somewhere, for instance on a Raspberry Pi
- Python > 3.7 and pip
- systemd supported Linux (e.g. Raspbian) if you want to use the installer in the release package

## Installation

The package comes with a reference `config.yaml` that you should adapt to your needs.

### Systemd

- Download and unpack the release in a directory of your choice, e.g. `/opt/mqtt2influx`
- Run `./install.sh` with `sudo` rights (since it creates a global systemd service)
- Start/Enable the service with `sudo systemctl start mqtt2influx.service`

### Manual

Of course you can also just install the `mqtt2influx` application and integrate it in whatever you want. For that, just download the package and install the wheel through
pip or pipx in e.g. a virtual environment.

## Uninstall

Navigate into your installation directory and run `./uninstall.sh`.
It will try to stop the service if it is running and will then delete the systemd service for you. Therefore you will also need to run it with `sudo` rights.

## Usage

Please refer to `mqtt2influx --help`.

## Contributing

See [here](CONTRIBUTING.md) if you would like to contribute. 
