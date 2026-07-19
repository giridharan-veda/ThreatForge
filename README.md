# ThreatForge

<p align="center">

<img src="docs/images/logo.png" alt="ThreatForge" width="180"/>

# ThreatForge

### An IoT Adversary Emulation Framework for Smart Home Cybersecurity Research

**ThreatForge** is an open-source cybersecurity research framework that enables realistic adversary emulation against Internet of Things (IoT) environments using **MITRE CALDERA**, **Node-RED**, and **Wazuh**. The framework provides a reproducible platform for evaluating detection capabilities, validating defensive controls, and conducting ATT&CK-aligned security research within simulated smart-home infrastructures.

---

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?logo=python&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-Supported-2496ED?logo=docker&logoColor=white)
![MITRE CALDERA](https://img.shields.io/badge/MITRE-CALDERA-red)
![Wazuh](https://img.shields.io/badge/Wazuh-005571)
![Node-RED](https://img.shields.io/badge/Node--RED-B22222?logo=nodered)
![Research](https://img.shields.io/badge/Research-Cybersecurity-success)
![License](https://img.shields.io/badge/License-MIT-green)

</p>

---

# Overview

ThreatForge is a modular adversary emulation framework designed specifically for **IoT security research**.

Traditional adversary emulation platforms primarily target enterprise Windows and Linux environments. ThreatForge extends this capability into smart-home IoT ecosystems by integrating custom adversary behaviors with simulated devices and security monitoring infrastructure.

The framework enables researchers, students, blue teams, and detection engineers to reproduce realistic attack scenarios while evaluating defensive visibility through the MITRE ATT&CK framework.

ThreatForge combines:

- MITRE CALDERA for adversary emulation
- Node-RED for IoT device simulation
- Wazuh for detection engineering
- Custom ThreatForge Agent for IoT protocol interaction
- Docker for reproducible deployment

---

# Key Features

- IoT-focused Adversary Emulation
- Custom MITRE CALDERA Agent
- ATT&CK-aligned Adversary Profiles
- Modular CALDERA Abilities
- Smart Home IoT Simulation
- MQTT, HTTP and SSH Attack Execution
- Wazuh Detection Engineering
- Automated Attack Chain Execution
- Reproducible Research Environment
- Docker-based Deployment

---

# Architecture

<p align="center">

<img src="paper/architecture/architecture.png" width="900">

</p>

```
                    +---------------------------+
                    |      MITRE CALDERA        |
                    | Adversary Emulation Engine|
                    +------------+--------------+
                                 |
                                 |
                                 ▼
                     +------------------------+
                     |   ThreatForge Agent    |
                     | Ability Execution Core |
                     +------------+-----------+
                                  |
          +-----------------------+-----------------------+
          |                       |                       |
          ▼                       ▼                       ▼
       HTTP API                 MQTT                    SSH
          |                       |                       |
          +-----------------------+-----------------------+
                                  |
                                  ▼
                     +----------------------------+
                     |     Node-RED Testbed       |
                     | Smart Home IoT Simulation  |
                     +-------------+--------------+
                                   |
                                   ▼
                          IoT Event Generation
                                   |
                                   ▼
                        +-----------------------+
                        |        Wazuh          |
                        | Detection & Monitoring|
                        +-----------------------+
```

---

# Repository Structure

```
ThreatForge/
│
├── paper/                 → Research Paper
├── docs/                  → Documentation
├── agent/                 → ThreatForge Agent
├── abilities/             → MITRE CALDERA Abilities
├── adversary/             → Adversary Profiles
├── testbed/               → Node-RED IoT Simulation
├── wazuh/                 → Detection Rules
├── docker/                → Docker Configuration
├── scripts/               → Helper Scripts
└── reports/               → Experimental Results
```

---

# Technology Stack

| Component | Purpose |
|------------|----------------------------------------------|
| MITRE CALDERA | Adversary Emulation |
| Python | ThreatForge Agent |
| Node-RED | Smart Home Simulation |
| MQTT | IoT Communication |
| HTTP | Device Interaction |
| SSH | Remote Command Execution |
| Wazuh | Detection & Monitoring |
| Docker | Environment Deployment |

---

# Experimental Workflow

```
Initialize Lab
        │
        ▼
Deploy Docker Environment
        │
        ▼
Start CALDERA
        │
        ▼
Register ThreatForge Agent
        │
        ▼
Import Adversary Profile
        │
        ▼
Execute Operation
        │
        ▼
Interact with IoT Devices
        │
        ▼
Generate Security Events
        │
        ▼
Detect using Wazuh
        │
        ▼
Collect Reports
```

---

# Supported Attack Simulation

ThreatForge currently supports the following IoT attack scenarios:

- Device Discovery
- Camera Snapshot Collection
- MQTT Command Injection
- Smart Lock Manipulation
- SSH Remote Execution
- Event Generation
- Detection Validation

Additional attack scenarios can be added by creating new CALDERA abilities and adversary profiles.

---

# Quick Start

Clone the repository.

```bash
git clone https://github.com/giridharan-veda/ThreatForge.git

cd ThreatForge
```

Install dependencies.

```bash
pip install -r requirements.txt
```

Run the setup script.

```bash
chmod +x scripts/setup.sh

./scripts/setup.sh
```

Start the laboratory.

```bash
docker compose up -d
```

Open:

```
MITRE CALDERA

Node-RED

Wazuh Dashboard
```

Execute the Hikvision adversary profile.

Monitor detections.

---

# Documentation

Detailed documentation is available under:

```
docs/
```

| Document | Description |
|-----------|-------------|
| setup-guide.md | Installation Guide |
| usage-guide.md | Running ThreatForge |
| README.md | Documentation Index |

---

# Research Paper

The complete research paper describing the architecture, implementation, methodology and evaluation is located under

```
paper/
```

---

# Project Objectives

ThreatForge aims to:

- Extend adversary emulation into IoT environments
- Improve defensive visibility
- Validate Wazuh detection capabilities
- Map attacks to MITRE ATT&CK
- Support reproducible cybersecurity research
- Facilitate purple-team exercises

---

# Intended Audience

ThreatForge is designed for:

- Cybersecurity Researchers
- SOC Analysts
- Detection Engineers
- Blue Teams
- Purple Teams
- Academic Institutions
- Security Students
- IoT Researchers

---

# Research Contributions

This project introduces:

- A custom IoT adversary emulation agent
- ATT&CK-aligned IoT attack chains
- Node-RED based smart-home simulation
- Wazuh detection engineering for IoT attacks
- A reproducible Docker-based research environment

---

# Citation

If you use ThreatForge in academic research, publications, or security evaluations, please cite this repository using the provided **CITATION.cff** file.

BibTeX and other citation formats are automatically generated by GitHub.

---

# Roadmap

Planned future enhancements include:

- Additional IoT device profiles
- BLE and Zigbee protocol support
- ICS/SCADA device simulation
- AI-assisted adversary planning
- Automated detection validation
- Multi-agent adversary emulation
- ATT&CK coverage expansion

---

# Contributing

Contributions are welcome.

If you would like to contribute:

1. Fork the repository.
2. Create a feature branch.
3. Commit your changes.
4. Submit a Pull Request.

For major changes, please open an Issue before implementation.

---

# Disclaimer

ThreatForge is developed **solely for educational, research, and authorized security testing purposes**.

The authors are **not responsible for any misuse** of this software. Users are responsible for ensuring compliance with applicable laws, organizational policies, and ethical guidelines.

---

# License

This project is licensed under the MIT License.

See the **LICENSE** file for additional information.

---

# Acknowledgements

ThreatForge builds upon several outstanding open-source cybersecurity projects and communities.

Special thanks to:

- MITRE CALDERA
- Wazuh
- Node-RED
- Docker
- Python Community

Their continued contributions have significantly advanced cybersecurity research and education.

---

<p align="center">

**ThreatForge — Forging Adversaries. Strengthening Defenders.**

</p>