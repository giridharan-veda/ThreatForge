#!/usr/bin/env python3
import sys, paho.mqtt.publish as publish
TOPIC = "home/bulb/command"
def main():
    if len(sys.argv) != 3:
        print(f"Usage: mqtt_exec.py <broker_host> <ON|OFF>")
        sys.exit(1)
    broker = sys.argv[1]
    message = sys.argv[2].upper()
    if message not in ("ON", "OFF"):
        print(f"Message must be ON or OFF, got: {message}")
        sys.exit(1)
    try:
        publish.single(TOPIC, message, hostname=broker, port=1883)
        print(f"MQTT published '{message}' to {TOPIC} on {broker}")
        sys.exit(0)
    except Exception as e:
        print(f"MQTT error: {e}")
        sys.exit(1)
if __name__ == "__main__":
    main()
