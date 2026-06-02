# MQTT Exercises 31-41

These files cover MQTT vs HTTP research, topic design, publisher/subscriber scripts, QoS examples, authentication/TLS configuration notes, IoT simulation, and threaded subscribers.

## MQTT vs HTTP

MQTT is a lightweight publish-subscribe protocol. Clients do not talk directly to each other; they publish messages to a broker and subscribe to topics. HTTP is request-response: a client asks a server for a resource and waits for a response. MQTT keeps connections open and is efficient for frequent small messages, while HTTP is better for web pages, APIs, and document-style requests.

MQTT is preferred for IoT telemetry, unreliable networks, battery-powered devices, and real-time sensor updates. HTTP is preferred for browser-based applications, REST APIs, and situations where each request is independent.

## Mosquitto Commands

```bash
mosquitto_sub -h localhost -t test/topic
mosquitto_pub -h localhost -t test/topic -m "Hello MQTT"
```

## Topic Structure

- `home/living-room/temperature`
- `home/living-room/humidity`
- `home/kitchen/temperature`
- wildcard single level: `home/+/temperature`
- wildcard multi level: `home/#`

## Security Notes

For production, configure Mosquitto with username/password authentication and TLS certificates. Test with valid client credentials before exposing a broker outside localhost.
