# ThreatForge Usage Guide

## Overview

This guide demonstrates how to execute the complete ThreatForge adversary emulation workflow.

The workflow consists of:

MITRE CALDERA

↓

ThreatForge Agent

↓

Node-RED IoT Testbed

↓

Wazuh Detection

↓

Reports

---

# Step 1 – Start the Environment

Start all services.

```bash
docker compose up -d
```

Verify:

```bash
docker ps
```

---

# Step 2 – Launch MITRE CALDERA

Open:

```
https://<CALDERA-IP>:8443
```

Log in using your administrator credentials.

---

# Step 3 – Verify Agent Registration

Navigate to:

```
Agents
```

Confirm the ThreatForge agent is online.

---

# Step 4 – Import the Adversary Profile

Navigate to:

```
Adversaries
```

Import:

```
adversary/Hikvision.yaml
```

---

# Step 5 – Create an Operation

Create a new operation.

Select:

- Planner
- ThreatForge Agent
- Hikvision Adversary Profile

Start the operation.

---

# Step 6 – Execute the Attack Chain

ThreatForge performs the following adversary actions:

1. Device Reconnaissance

2. Camera Snapshot Collection

3. Smart Lock Manipulation

4. MQTT Device Interaction

5. SSH-based Lateral Movement

6. Event Logging

---

# Step 7 – Monitor the IoT Testbed

Observe the simulated device interactions within Node-RED.

Example endpoints:

```
GET  /api/devices

POST /api/camera/snapshot

POST /api/lock/unlock

MQTT home/bulb/command
```

---

# Step 8 – Monitor Wazuh

Open the Wazuh Dashboard.

Verify alerts corresponding to:

- Discovery
- Collection
- Lateral Movement
- Impact

Confirm events are mapped to the MITRE ATT&CK framework where applicable.

---

# Step 9 – Review CALDERA Results

After the operation completes:

Open the Operation Report.

Review:

- Successful Abilities
- Failed Abilities
- Execution Timeline

---

# Step 10 – Export Results

Save:

- CALDERA Operation Report
- Wazuh Alerts
- Node-RED Event Logs

Store exported files under:

```
reports/
```

---

# Shutdown

Stop the environment.

```bash
docker compose down
```

---

# Expected Outcome

A successful execution demonstrates:

- Adversary emulation using MITRE CALDERA
- Interaction with a simulated IoT environment
- Detection by Wazuh
- Correlation of adversary actions to ATT&CK techniques
- Collection of reproducible experimental evidence

---

# Additional Resources

For installation instructions:

```
setup-guide.md
```

For research details:

```
../paper/
```
