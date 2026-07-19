# ThreatForge Setup Guide

## Overview

This document describes the installation and configuration process for ThreatForge.

ThreatForge is designed to emulate Advanced Persistent Threat (APT) techniques against simulated IoT environments using MITRE CALDERA while validating detections through Wazuh.

---

# System Requirements

Recommended operating system:

- Kali Linux
- Ubuntu 22.04 or later

Hardware:

- 4 CPU Cores
- 8 GB RAM minimum
- Docker-compatible system

Software:

- Git
- Docker
- Docker Compose
- Python 3.10+
- pip

---

# Step 1 – Clone the Repository

```bash
git clone https://github.com/giridharan-veda/ThreatForge.git

cd ThreatForge
```

---

# Step 2 – Install Python Dependencies

```bash
pip install -r requirements.txt
```

---

# Step 3 – Configure the Agent

Copy the example configuration.

```bash
cp agent/agent.env.example agent/agent.env
```

Edit the configuration according to your environment.

Update:

- CALDERA Server
- MQTT Broker
- Agent Group
- Authentication Settings

---

# Step 4 – Deploy Supporting Services

If Docker is used:

```bash
docker compose up -d
```

Verify:

```bash
docker ps
```

All required services should be running.

---

# Step 5 – Configure Node-RED

Open the Node-RED Editor.

Import:

```
testbed/iot_sim.json
```

Deploy the flow.

Confirm all HTTP endpoints are active.

---

# Step 6 – Configure Wazuh

Copy:

```
wazuh/rules/local_rules_merged.xml
```

into the Wazuh rules directory.

Restart the Wazuh Manager.

Verify that the rules load successfully.

---

# Step 7 – Configure MITRE CALDERA

Copy:

```
abilities/
```

and

```
adversary/
```

into the appropriate CALDERA directories.

Restart CALDERA.

---

# Step 8 – Verify Installation

Ensure:

✓ CALDERA is accessible

✓ Node-RED is running

✓ Wazuh Manager is running

✓ ThreatForge Agent connects successfully

✓ Testbed endpoints respond correctly

---

# Troubleshooting

## Agent Not Connecting

Verify:

- Server URL
- Credentials
- Firewall
- SSL Configuration

---

## Node-RED Flow Not Working

Verify:

- Flow imported correctly
- Deploy button pressed
- Correct listening port

---

## Wazuh Not Detecting Events

Verify:

- Rules copied successfully
- Wazuh restarted
- Event logs are generated

---

# Next Step

Proceed to:

```
usage-guide.md
```

to execute the attack chain.
