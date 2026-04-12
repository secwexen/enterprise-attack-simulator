# Enterprise Attack Simulator

[![Coverage](https://codecov.io/gh/secwexen/enterprise-attack-simulator/branch/main/graph/badge.svg?branch=main&event=pull_request)](https://codecov.io/gh/secwexen/enterprise-attack-simulator)
[![License](https://img.shields.io/github/license/secwexen/enterprise-attack-simulator)](https://github.com/secwexen/enterprise-attack-simulator/blob/main/LICENSE)

## About

Enterprise Attack Simulator is a modular, MITRE ATT&CK–aligned adversary simulation framework that empowers Red Teams, Purple Teams, and security engineers to test and enhance enterprise security defenses. It simulates realistic attack chains on Windows and Linux environments, providing actionable insights through structured reports.

## Overview

Enterprise Attack Simulator is a modular adversary simulation framework designed to emulate real-world attack scenarios based on the MITRE ATT&CK framework. It enables Red Teams, Purple Teams, and security engineers to safely execute controlled attack chains across Windows and Linux environments.

By combining YAML-defined attack profiles with an extensible technique architecture, the framework allows users to model complex attack paths, validate defensive controls, and identify detection gaps. Built-in reporting and logging capabilities provide actionable insights to strengthen security posture and improve incident response readiness.

## Features

- Full **MITRE ATT&CK–aligned** tactics and techniques  
- Modular and extensible technique architecture  
- Windows & Linux technique support  
- YAML-based attack profiles  
- Automatic reporting (JSON + Markdown)  
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
├── CODE_OF_CONDUCT.md
├── LICENSE
├── README.md
├── SECURITY.md
└── requirements.txt
```

## Installation

```bash
# Clone repository
git clone https://github.com/secwexen/enterprise-attack-simulator.git
cd enterprise-attack-simulator

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

# Install dependencies
pip install -r requirements.txt

# Install dev dependencies
pip install -r dev-requirements.txt
```

## Usage

### CLI Options

`--profile`          Specify attack profile YAML file to execute  
`--verbose`          Enable detailed logging  
`--dry-run`          Simulate attacks without executing actions  

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
See the [LICENSE](/LICENSE) file for full details.

## Security

For guidance on safe usage and reporting vulnerabilities, see [SECURITY.md](/SECURITY.md).

## Development Status

**Enterprise Attack Simulator** is currently in **Early Development / Beta** stage.

## Author

**Secwexen** – Project Author, Lead & Maintainer    
**GitHub:** [github.com/secwexen](https://github.com/secwexen)
