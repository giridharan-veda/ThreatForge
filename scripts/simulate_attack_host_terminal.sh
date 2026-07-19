#!/usr/bin/env bash
#
# Simulates the IoT attack chain to trigger Wazuh rules 100100, 100110,
# 100120, 100121, 100130.
#
# Adjust the variables below to match your Node-RED setup before running.

set -e

NODE_RED_URL="http://localhost:1880"     # base URL of your Node-RED HTTP endpoints
MQTT_BROKER="localhost"                   # MQTT broker host
MQTT_PORT="1883"
MQTT_TOPIC="home/bulb/command"

echo "=== [1/5] Recon: GET /api/devices  -> expect rule 100100 ==="
curl -s -X GET "${NODE_RED_URL}/api/devices" -o /dev/null -w "HTTP %{http_code}\n"
sleep 2

echo "=== [2/5] Exfiltration: GET /api/camera/snapshot -> expect rule 100110 ==="
# NOTE: rule 100110 fires on large_response=true. This flag must be set by
# your Node-RED flow itself (e.g. response body > some KB threshold) and
# written into events.log — a curl request alone doesn't set it. Trigger
# the flow, then confirm events.log shows "large_response":"true".
curl -s -X GET "${NODE_RED_URL}/api/camera/snapshot" -o /tmp/snapshot.jpg -w "HTTP %{http_code}\n"
sleep 2

echo "=== [3/5] Impact (failure): wrong PIN -> expect rule 100121 ==="
curl -s -X POST "${NODE_RED_URL}/api/lock/unlock" \
  -H "Content-Type: application/json" \
  -d '{"pin_attempt":"0000"}' -w "\nHTTP %{http_code}\n"
sleep 2

echo "=== [4/5] Impact (success): correct PIN -> expect rule 100120 ==="
curl -s -X POST "${NODE_RED_URL}/api/lock/unlock" \
  -H "Content-Type: application/json" \
  -d '{"pin_attempt":"1234"}' -w "\nHTTP %{http_code}\n"
sleep 2

echo "=== [5/5] Manipulation: MQTT publish to bulb -> expect rule 100130 ==="
# requires mosquitto-clients: apt install -y mosquitto-clients
mosquitto_pub -h "${MQTT_BROKER}" -p "${MQTT_PORT}" -t "${MQTT_TOPIC}" -m '{"state":"on"}'

echo ""
echo "Simulation complete. Check events.log on the Node-RED host:"
echo "  tail -n 20 /path/to/node-red/events.log"
echo ""
echo "Then check the Wazuh manager picked them up:"
echo "  docker exec single-node-wazuh.manager-1 tail -f /var/ossec/logs/alerts/alerts.log | grep -A5 iot_attack"
