# MQTT Exercises 31-41

This folder turns the MQTT exercises into a small IoT communication package. It includes the written comparison, topic design, publisher/subscriber scripts, QoS examples, security notes, and concurrency-ready subscriber logic.

## MQTT vs HTTP

MQTT is a lightweight publish-subscribe protocol. A device publishes data to a broker, and any interested client subscribes to matching topics. HTTP is request-response: a client sends a request and waits for a server response.

MQTT is preferred for IoT because sensors often send small messages repeatedly. It is efficient for low-bandwidth networks, real-time updates, and many devices publishing to the same broker. HTTP is better for websites, REST APIs, file transfers, and independent one-time requests.

## Topic Design

The topic structure is designed like a smart home:

- `home/living-room/temperature`
- `home/living-room/humidity`
- `home/kitchen/temperature`
- `home/bedroom/temperature`

Wildcards:

- `home/+/temperature` subscribes to temperature from any one room.
- `home/#` subscribes to everything inside the home namespace.

This topic structure is more scalable than using one topic like `temperature`, because every message carries location meaning.

## Implementation Choices

- `publisher.py` sends both plain text and JSON sensor payloads.
- `subscriber.py` uses callback functions because MQTT is event-driven.
- QoS values can be changed in the publish calls to test delivery guarantees.
- Threaded subscribers are included to demonstrate concurrent message handling.
- Logging is used instead of plain `print()` for received messages because timestamps are useful in communication systems.

## Mosquitto Test Commands

```bash
mosquitto_sub -h localhost -t test/topic
mosquitto_pub -h localhost -t test/topic -m "Hello MQTT"
```

## Security Notes

For production, the broker should require username/password authentication and TLS encryption. This protects messages from unauthorized clients and prevents sensor data from being sent in plain text.

## Run

```bash
pip install paho-mqtt
python subscriber.py
python publisher.py
```
