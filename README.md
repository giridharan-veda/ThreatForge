<div align="center">

# ThreatForge

**An IoT Adversary Emulation Framework for Smart Home Cybersecurity Research**

Reproducible, ATT&CK-aligned adversary emulation for smart-home IoT environments — built on **MITRE CALDERA**, **Node-RED**, and **Wazuh**.

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Docker](https://img.shields.io/badge/Docker-Supported-2496ED?logo=docker&logoColor=white)](https://www.docker.com/)
[![MITRE CALDERA](https://img.shields.io/badge/MITRE-CALDERA-red)](https://caldera.mitre.org/)
[![Wazuh](https://img.shields.io/badge/Wazuh-005571?logo=wazuh&logoColor=white)](https://wazuh.com/)
[![Node-RED](https://img.shields.io/badge/Node--RED-B22222?logo=nodered&logoColor=white)](https://nodered.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](#contributing)

[Overview](#overview) •
[Features](#key-features) •
[Architecture](#architecture) •
[Quick Start](#quick-start) •
[Documentation](#documentation) •
[Roadmap](#roadmap)

</div>

---

## Overview

Most adversary emulation platforms target enterprise Windows and Linux infrastructure. **ThreatForge** extends that same rigor into the **smart-home IoT space**, giving researchers, students, and blue teams a reproducible environment to emulate attacker behavior, generate realistic telemetry, and validate detection coverage against the **MITRE ATT&CK** framework.

ThreatForge integrates:

- **MITRE CALDERA** — adversary emulation and operation orchestration
- **Node-RED** — smart-home device and protocol simulation
- **Wazuh** — detection engineering, log analysis, and alerting
- **ThreatForge Agent** — a custom CALDERA agent purpose-built for IoT protocol interaction
- **Docker** — one-command, reproducible lab deployment

The result is an end-to-end pipeline: launch an attack chain against simulated smart-home devices, observe the resulting telemetry, and measure how well your detection stack catches it.

---

## Key Features

| Category | Capability |
|---|---|
| **Emulation** | IoT-focused adversary emulation via a custom MITRE CALDERA agent |
| **Coverage** | ATT&CK-aligned adversary profiles and modular CALDERA abilities |
| **Simulation** | Realistic smart-home IoT testbed powered by Node-RED |
| **Protocols** | Native support for MQTT, HTTP, and SSH attack execution |
| **Detection** | Wazuh-based detection engineering and rule validation |
| **Automation** | Fully automated, repeatable attack-chain execution |
| **Reproducibility** | Docker-based deployment for consistent research environments |

---

## Architecture

```
┌──────────────────────────────┐
│         MITRE CALDERA        │
│  Adversary Emulation Engine  │
└───────────────┬───────────────┘
                │
                ▼
┌──────────────────────────────┐
│       ThreatForge Agent      │
│    Ability Execution Core    │
└───────────────┬───────────────┘
                │
   ┌────────────┼────────────┐
   ▼            ▼            ▼
 HTTP API      MQTT          SSH
   │            │            │
   └────────────┼────────────┘
                ▼
┌──────────────────────────────┐
│        Node-RED Testbed      │
│  Smart-Home IoT Simulation   │
└───────────────┬───────────────┘
                │
                ▼
        IoT Event Generation
                │
                ▼
┌──────────────────────────────┐
│             Wazuh            │
│   Detection & Monitoring     │
└──────────────────────────────┘
```

**Flow:** CALDERA orchestrates operations → the ThreatForge Agent executes abilities against the testbed over HTTP, MQTT, or SSH → Node-RED simulates smart-home device responses and emits IoT events → Wazuh ingests and analyzes the resulting telemetry for detection validation.

---

## Repository Structure

```
ThreatForge/
├── paper/          Research paper (architecture, methodology, evaluation)
├── docs/            Documentation (setup, usage, reference)
├── agent/           ThreatForge Agent source
├── abilities/       MITRE CALDERA abilities
├── adversary/        Adversary profiles
├── testbed/          Node-RED smart-home IoT simulation
├── wazuh/            Detection rules and configuration
├── docker/           Docker & container configuration
├── scripts/          Setup and helper scripts
└── reports/          Experimental results
```

---

## Technology Stack

| Component | Role |
|---|---|
| MITRE CALDERA | Adversary emulation and operation management |
| Python | ThreatForge Agent implementation |
| Node-RED | Smart-home device simulation |
| MQTT | IoT device communication protocol |
| HTTP | Device interaction and API layer |
| SSH | Remote command execution |
| Wazuh | Detection, monitoring, and alerting |
| Docker | Reproducible environment deployment |

---

## Supported Attack Scenarios

- Device discovery and enumeration
- Camera snapshot collection
- MQTT command injection
- Smart lock manipulation
- SSH-based remote execution
- Security event generation
- End-to-end detection validation

Additional scenarios can be added by creating new CALDERA abilities and adversary profiles — see [Contributing](#contributing).

---

## Quick Start

**1. Clone the repository**

```bash
git clone https://github.com/giridharan-veda/ThreatForge.git
cd ThreatForge
```

**2. Install dependencies**

```bash
pip install -r requirements.txt
```

**3. Run the setup script**

```bash
chmod +x scripts/setup.sh
./scripts/setup.sh
```

**4. Launch the lab**

```bash
docker compose up -d
```

**5. Open the consoles**

| Service | Purpose |
|---|---|
| MITRE CALDERA | Operation control and adversary management |
| Node-RED | IoT testbed visualization |
| Wazuh Dashboard | Detection monitoring and alerting |

**6. Run an operation**

Execute the Hikvision adversary profile and monitor detections in real time via the Wazuh dashboard.

---

## Documentation

Full documentation lives under [`docs/`](docs/):

| Document | Description |
|---|---|
| `setup-guide.md` | Full installation and configuration guide |
| `usage-guide.md` | Running operations with ThreatForge |
| `README.md` | Documentation index |

The complete research paper — covering architecture, implementation, methodology, and evaluation — is available under [`paper/`](paper/).

---

## Project Objectives

- Extend adversary emulation into IoT environments
- Improve defensive visibility for smart-home ecosystems
- Validate Wazuh detection capabilities against realistic attack chains
- Map IoT attack behavior to MITRE ATT&CK
- Support reproducible, citable cybersecurity research
- Facilitate purple-team exercises

## Intended Audience

Cybersecurity researchers · SOC analysts · detection engineers · blue & purple teams · academic institutions · security students · IoT researchers

---

## Roadmap

- [ ] Additional IoT device profiles
- [ ] BLE and Zigbee protocol support
- [ ] ICS/SCADA device simulation
- [ ] AI-assisted adversary planning
- [ ] Automated detection validation
- [ ] Multi-agent adversary emulation
- [ ] Expanded ATT&CK coverage

---

## Contributing

Contributions are welcome and appreciated.

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Open a Pull Request

For significant changes, please open an Issue first to discuss the proposed direction.

---

## Citation

If you use ThreatForge in academic research, publications, or security evaluations, please cite this repository using the included [`CITATION.cff`](CITATION.cff). BibTeX and other citation formats are generated automatically by GitHub.

---

## Disclaimer

ThreatForge is developed **solely for educational, research, and authorized security testing purposes**. The authors are not responsible for any misuse of this software. Users are responsible for ensuring compliance with all applicable laws, organizational policies, and ethical guidelines.

---

## License

Licensed under the [MIT License](LICENSE).

## Acknowledgements

ThreatForge builds on the work of outstanding open-source projects and communities, including MITRE CALDERA, Wazuh, Node-RED, Docker, and the broader Python community.

<div align="center">

**ThreatForge — Forging Adversaries. Strengthening Defenders.**

</div>
