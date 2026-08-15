# Security Policy

ThreatForge is an open-source IoT adversary emulation and detection validation platform designed for authorised security testing, controlled laboratory environments, purple-team exercises, detection engineering, and cybersecurity research.

Security issues affecting ThreatForge are taken seriously. We encourage responsible disclosure so vulnerabilities can be assessed and addressed without unnecessary public exposure.

## Supported Versions

Security fixes are provided for the latest stable release series.

| Version | Supported |
|---|---|
| `v1.x` | :white_check_mark: |
| `< v1.0` | :x: |

Only official stable releases are covered by this policy. Development snapshots, forks, and modified deployments are outside the supported-version policy.

## Reporting a Vulnerability

### Preferred Reporting Method

Please report suspected security vulnerabilities through **GitHub Private Vulnerability Reporting** rather than opening a public GitHub Issue.

Private reporting helps prevent sensitive vulnerability details from being disclosed before an appropriate fix or mitigation is available.

### What to Include

Please provide, where possible:

- A clear description of the vulnerability
- The affected ThreatForge version or commit
- The affected component, file, configuration, or deployment path
- Steps required to reproduce the issue
- Expected and actual behaviour
- Potential security impact
- Relevant logs, screenshots, traces, or proof-of-concept material
- Suggested remediation or mitigation, if available

Please remove passwords, API keys, private keys, tokens, personal information, and other sensitive data before submitting supporting material.

## What to Expect

Reported vulnerabilities will be reviewed for reproducibility, security impact, and affected scope.

Where additional information is required, the reporter may be contacted for clarification. Confirmed issues may result in a code change, configuration change, mitigation, or patched release as appropriate.

Reports may be closed when an issue cannot be reproduced, does not present a security impact, falls outside the project scope, or is caused entirely by an unrelated third-party component.

Response and remediation times may vary depending on severity, complexity, and the availability of an appropriate fix.

## Disclosure Policy

Please do not publicly disclose vulnerability details before a fix or mitigation has been coordinated with the maintainer.

After an appropriate remediation is available, disclosure may be coordinated with the reporter where appropriate.

## Security Scope

Security reports are relevant to vulnerabilities in ThreatForge-maintained components, including:

- ThreatForge source code and distributed components
- ThreatForge Agent and its protocol executors
- CALDERA abilities and the `Custom IoT Adversary` profile
- Node-RED testbed components maintained by ThreatForge
- Wazuh detection and integration configuration maintained by ThreatForge
- Deployment configuration and supporting scripts

ThreatForge intentionally includes adversary-emulation capabilities such as device discovery, camera interaction, smart-lock manipulation, MQTT control, and SSH-based lateral movement. These behaviours are **intended functionality** and are not vulnerabilities by themselves.

Issues in third-party software such as MITRE CALDERA, Wazuh, Node-RED, Docker, Python, operating systems, or external dependencies should normally be reported to the relevant upstream project. However, vulnerabilities in ThreatForge's integration, configuration, implementation, or interaction with those components remain within scope.

## Safe Testing Requirements

ThreatForge is a security testing platform. Testing must only be performed against systems, devices, networks, and environments for which you have explicit authorisation.

Do not use ThreatForge to:

- Access or attack systems without permission
- Target third-party consumer or enterprise devices
- Disrupt production services
- Expose or obtain credentials or sensitive information
- Conduct activity intended to cause real-world harm

The included smart-home environment is designed to support controlled security testing without requiring attacks against physical consumer IoT devices.

## Security Best Practices for Users

Users deploying ThreatForge should:

- Run the platform in an isolated or controlled environment
- Use test credentials rather than production credentials
- Avoid exposing CALDERA, Node-RED, Wazuh, or agent services to untrusted networks
- Keep the operating system, Docker environment, Python packages, and integrated security tools updated
- Review configuration files before deployment
- Never commit passwords, credentials, private keys, tokens, or sensitive environment files

## Third-Party Dependencies

ThreatForge integrates with third-party security and infrastructure components, including MITRE CALDERA, Wazuh, Node-RED, Docker, Python, HTTP, MQTT, and SSH.

Users should monitor relevant upstream security advisories and keep dependencies appropriately updated.

## Security Updates

Confirmed security issues may be addressed through:

- A patched software release
- Configuration or deployment changes
- Mitigation guidance
- Updates to documentation
- Security-related release notes

## Credit

Responsible disclosure contributors may be credited for reported vulnerabilities when appropriate and with their permission.

Thank you for helping keep ThreatForge and its users secure.

## Contact

For vulnerability reports, please use **GitHub Private Vulnerability Reporting**:

**Repository → Security → Advisories → Report a vulnerability**

For general bugs, documentation issues, and feature requests, please use GitHub Issues or Pull Requests.
