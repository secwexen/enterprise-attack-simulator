# Enterprise Attack Simulator

[![License](https://img.shields.io/github/license/secwexen/enterprise-attack-simulator?branch=main)](https://github.com/secwexen/enterprise-attack-simulator/blob/main/LICENSE)
[![Status](https://img.shields.io/badge/status-active-success)](https://github.com/secwexen/enterprise-attack-simulator)

A modular adversary simulation framework designed to emulate real-world cyber attacks based on the MITRE ATT&CK framework.  
This project enables Red Team, Purple Team, and security engineers to evaluate detection capabilities, validate defensive controls, and simulate realistic attack chains in enterprise environments.

## About

Enterprise Attack Simulator is a modular, MITRE ATT&CK–aligned adversary simulation framework that empowers Red Teams, Purple Teams, and security engineers to test and enhance enterprise security defenses. It simulates realistic attack chains on Windows and Linux environments, providing actionable insights through structured reports.

## Overview

This framework is designed for realistic cyberattack simulation in enterprise environments. Its modular architecture allows easy extension of attack techniques, supporting both Windows and Linux systems. Users can define attack chains via YAML profiles, run them safely in dry-run mode, and generate detailed JSON and Markdown reports for detection validation and defense assessment. By leveraging MITRE ATT&CK techniques, organizations can improve threat detection, response strategies, and security posture.

## Features

- Full **MITRE ATT&CK–aligned** tactics and techniques  
- Modular and extensible technique architecture  
- Windows & Linux technique support  
- YAML-based attack profiles  
- Automatic reporting (JSON + Markdown)  
- Developer-friendly technique creation guide  
- Logging and behavioral tracking hooks  

## Architecture Overview

The framework is built around three core components:

### 1. Core Engine

- Loads and executes attack techniques  
- Manages execution flow  
- Generates structured reports  

### 2. Techniques Module

- Each MITRE ATT&CK technique is implemented as an independent module  
- Easy to extend and customize  
- Supports multiple platforms  

### 3. Attack Profiles

- YAML files define attack chains  
- Example: Discovery → Persistence → Lateral Movement  

## Project Structure

```
enterprise-attack-simulator/
│
├── src/
│   ├── core/
│   │   ├── executor.py
│   │   ├── technique_loader.py
│   │   └── report_generator.py
│   │
│   ├── techniques/
│   │   ├── discovery/
│   │   │   └── T1087_list_users.py
│   │   ├── persistence/
│   │   │   └── T1053_scheduled_tasks.py
│   │   └── lateral_movement/
│   │       └── T1021_remote_services.py
│   │
│   ├── utils/
│   │   ├── logger.py
│   │   ├── system_checks.py
│   │   └── platform_detection.py
│   │
│   └── main.py
│
├── configs/
│   ├── attack_profile_example.yaml
│   └── technique_mapping.json
│
├── reports/
│   └── (auto-generated reports)
│
├── tests/
│   ├── test_executor.py
│   ├── test_techniques.py
│   └── test_utils.py
│
├── LICENSE
├── README.md
└── requirements.txt
```

## Installation

```bash
git clone https://github.com/secwexen/enterprise-attack-simulator.git
cd enterprise-attack-simulator
pip install -r requirements.txt
```

## Usage

### CLI Options

--profile <path>   Specify attack profile YAML file to execute  
--verbose          Enable detailed logging  
--dry-run          Simulate attacks without executing actions  

Run an attack profile:

```bash
python src/main.py --profile configs/attack_profile_example.yaml
```

## Running Tests

```bash
pytest tests/
```

## Disclaimer

This tool is intended for authorized security testing, research, and educational purposes only.
Unauthorized use against systems without explicit permission is illegal and strictly prohibited.
The authors are not responsible for misuse.

## License

Copyright © 2026 secwexen.

This project is licensed under the **Apache-2.0 License**.  
See the [LICENSE](LICENSE) file for full details.

## Security

For guidance on safe usage and reporting vulnerabilities, see [SECURITY.md](/SECURITY.md).

## Development Status

**Enterprise Attack Simulator** is currently in **Early Development / Beta** stage.

## Author

**Secwexen** – Project Author, Lead & Maintainer  
**GitHub:** [github.com/secwexen](https://github.com/secwexen)  
