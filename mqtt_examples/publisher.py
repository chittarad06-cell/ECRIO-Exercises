"""Exercises 34, 35, 38, and 40: MQTT publisher examples."""

import json
import random
import time

try:
    import paho.mqtt.client as mqtt
except ImportError:
    mqtt = None


BROKER = "localhost"
TOPICS = ["test/topic", "sensors/temperature"]


def publish_message(topic="test/topic", payload="Hello MQTT", qos=0):
    if not mqtt:
        print("Install paho-mqtt first: pip install paho-mqtt")
        return

    client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
    client.connect(BROKER, 1883, 60)
    client.publish(topic, payload, qos=qos)
    client.disconnect()


def publish_sensor_loop(iterations=5):
    if not mqtt:
        print("Install paho-mqtt first: pip install paho-mqtt")
        return

    client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
    client.connect(BROKER, 1883, 60)
    for _ in range(iterations):
        payload = {"sensor": "temperature", "value": round(random.uniform(20, 35), 2)}
        client.publish("sensors/temperature", json.dumps(payload), qos=1)
        time.sleep(1)
    client.disconnect()


if __name__ == "__main__":
    publish_message("test/topic", "Hello from Exercise 34", qos=0)
    publish_message("sensors/temperature", json.dumps({"sensor": "temperature", "value": 25}), qos=1)
