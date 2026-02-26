# **Enterprise Attack Simulator**

![License](https://img.shields.io/github/license/secwexen/enterprise-attack-simulator)

A modular adversary simulation framework designed to emulate real-world cyber attacks based on the MITRE ATT&CK framework.  
This project enables Red Team, Purple Team, and security engineers to evaluate detection capabilities, validate defensive controls, and simulate realistic attack chains in enterprise environments.

---

## **Features**

- Full **MITRE ATT&CK–aligned** tactics and techniques  
- Modular and extensible technique architecture  
- Windows & Linux technique support  
- YAML-based attack profiles  
- Automatic reporting (JSON + Markdown)  
- Developer-friendly technique creation guide  
- Logging and behavioral tracking hooks  

---

## **Architecture Overview**

The framework is built around three core components:

### **1. Core Engine**
- Loads and executes attack techniques  
- Manages execution flow  
- Generates structured reports  

### **2. Techniques Module**
- Each MITRE ATT&CK technique is implemented as an independent module  
- Easy to extend and customize  
- Supports multiple platforms  

### **3. Attack Profiles**
- YAML files define attack chains  
- Example: Discovery → Persistence → Lateral Movement  

---

## **Project Structure**

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
├── .gitignore
├── LICENSE
├── README.md
└── requirements.txt
```

---

## **Installation**

```bash
git clone https://github.com/secwexen/enterprise-attack-simulator.git
cd enterprise-attack-simulator
pip install -r requirements.txt
```

---

## **Usage**

### CLI Options

--profile <path>   Specify attack profile YAML file to execute  
--verbose          Enable detailed logging  
--dry-run          Simulate attacks without executing actions  

Run an attack profile:

```bash
python src/main.py --profile configs/attack_profile_example.yaml
```

---

## **Running Tests**

```bash
pytest tests/
```

---

## Disclaimer

This tool is intended for authorized security testing, research, and educational purposes only.
Unauthorized use against systems without explicit permission is illegal and strictly prohibited.
The authors are not responsible for misuse.

---

## **License**

This project is licensed under the **Apache-2.0 License**.  
See the [LICENSE](LICENSE) file for full details.

---

## Author

**Secwexen** – Project Author & Maintainer  
**GitHub:** [github.com/secwexen](https://github.com/secwexen)  
