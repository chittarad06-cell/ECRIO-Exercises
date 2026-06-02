"""Exercises 36, 37, 38, 40, and 41: MQTT subscriber examples."""

import logging
import threading

try:
    import paho.mqtt.client as mqtt
except ImportError:
    mqtt = None


logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(message)s")
BROKER = "localhost"


def on_connect(client, userdata, flags, reason_code, properties=None):
    logging.info("Connected with result code: %s", reason_code)
    client.subscribe("test/topic", qos=0)
    client.subscribe("sensors/#", qos=1)


def on_message(client, userdata, message):
    logging.info("Topic: %s | Payload: %s", message.topic, message.payload.decode())


def on_subscribe(client, userdata, mid, reason_codes, properties=None):
    logging.info("Subscription acknowledged: %s", mid)


def start_subscriber():
    if not mqtt:
        print("Install paho-mqtt first: pip install paho-mqtt")
        return

    client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
    client.on_connect = on_connect
    client.on_message = on_message
    client.on_subscribe = on_subscribe
    client.connect(BROKER, 1883, 60)
    client.loop_forever()


def start_threaded_subscribers(count=2):
    threads = []
    for _ in range(count):
        thread = threading.Thread(target=start_subscriber, daemon=True)
        thread.start()
        threads.append(thread)
    return threads


if __name__ == "__main__":
    start_subscriber()
