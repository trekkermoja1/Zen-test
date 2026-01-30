# 🛡️ Zen AI Pentest

**AI-Powered Multi-LLM Penetration Testing Intelligence System**

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Author](https://img.shields.io/badge/Author-SHAdd0WTAka-red.svg)](#)

> ⚠️ **DISCLAIMER**: This tool is for authorized security testing only. Always obtain proper permission before testing any systems you do not own.

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Architecture](#architecture)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Modules](#modules)
- [CVE & Ransomware Database](#cve--ransomware-database)
- [SQL Injection Database](#sql-injection-database)
- [Nuclei Integration](#nuclei-integration)
- [API Backends](#api-backends)
- [Contributing](#contributing)
- [Contributors](#contributors)

## 🎯 Overview

Zen AI Pentest is an advanced penetration testing framework that leverages multiple Large Language Models (LLMs) to assist security professionals in reconnaissance, vulnerability analysis, exploit assistance, and report generation. The system intelligently routes requests across free and authenticated LLM backends to maximize efficiency and minimize API costs.

### Key Highlights

- 🔗 **Multi-LLM Integration** - Seamlessly switches between DuckDuckGo AI, OpenRouter, ChatGPT, and Claude
- 🤖 **Multi-Agent System** - Clawed/Moltbot-style agents that collaborate, share context, and conduct research
- 🧠 **AI-Powered Analysis** - Intelligent vulnerability detection and exploit suggestion
- 📊 **Comprehensive Databases** - Built-in CVE, Ransomware, and SQL Injection payload databases
- 🔍 **Nuclei Integration** - Automated vulnerability scanning with Nuclei templates
- 📄 **Automated Reporting** - Generate professional pentest reports in multiple formats
- 🎭 **Stealth Operations** - Built-in stealth features for covert testing
- ⚡ **Async Architecture** - High-performance asynchronous operations
- 🔧 **Modular Design** - Easy to extend with custom modules

## ✨ Features

### Core Features

| Feature | Description | Status |
|---------|-------------|--------|
| Multi-LLM Routing | Automatic backend selection based on quality requirements | ✅ |
| Reconnaissance | AI-powered target reconnaissance and attack vector identification | ✅ |
| Vulnerability Analysis | Intelligent analysis of scan results (nmap, web headers, etc.) | ✅ |
| Exploit Assistance | Payload generation and exploit technique suggestions | ✅ |
| **CVE Database** | Comprehensive CVE and ransomware database (NotPetya, WannaCry, etc.) | ✅ |
| **SQL Injection DB** | 50+ payloads for 6 database types | ✅ |
| **Nuclei Integration** | Template management and automated scanning | ✅ |
| **Multi-Agent System** | Clawed/Moltbot-style collaborative agents | ✅ |
| **WordPress Templates** | Nuclei templates for WordPress pentesting | ✅ |
| Report Generation | Professional markdown, JSON, CSV, and HTML reports | ✅ |
| Session Management | Persistent sessions for authenticated backends | ✅ |
| Stealth Mode | Random delays, user-agent rotation, and evasion techniques | ✅ |
| Interactive CLI | User-friendly command-line interface | ✅ |

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                        Zen AI Pentest                           │
├─────────────────────────────────────────────────────────────────┤
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────────────┐  │
│  │    Recon     │  │  Vuln Scan   │  │   Exploit Assist     │  │
│  │    Module    │  │   Module     │  │      Module          │  │
│  └──────┬───────┘  └──────┬───────┘  └──────────┬───────────┘  │
│         └──────────────────┼─────────────────────┘              │
│                            │                                    │
│         ┌──────────────────┼──────────────────┐                │
│         │                  │                  │                 │
│  ┌──────┴──────┐  ┌────────┴────────┐  ┌─────┴──────┐          │
│  │   CVE DB    │  │   SQLi DB       │  │  Nuclei    │          │
│  │ (Ransomware)│  │ (Payloads)      │  │ Integration│          │
│  └──────┬──────┘  └────────┬────────┘  └─────┬──────┘          │
│         └──────────────────┼──────────────────┘                 │
│                            │                                    │
│                     ┌──────┴──────┐                            │
│                     │ZenOrchestrator│                           │
│                     │   (Router)    │                           │
│                     └──────┬──────┘                            │
│                            │                                    │
│         ┌──────────────────┼──────────────────┐                │
│         │                  │                  │                 │
│    ┌────┴────┐       ┌────┴────┐       ┌────┴────┐            │
│    │   DDG   │       │OpenRouter│       │ Direct  │            │
│    │  (Free) │       │Free Tier │       │  APIs   │            │
│    └─────────┘       └─────────┘       └─────────┘            │
└─────────────────────────────────────────────────────────────────┘
```

## 📦 Installation

### Prerequisites

- Python 3.8 or higher (3.13+ on Windows see note below)
- pip or pip3
- Nuclei (optional, for vulnerability scanning)

> **⚠️ Windows + Python 3.13+ Note:**  
> If you encounter `_ProactorBasePipeTransport._call_connection_lost` errors on Windows with Python 3.13+, the tool includes automatic fixes. These errors are harmless and have been patched in the code.

### Quick Install

```bash
# Clone the repository
git clone https://github.com/SHAdd0WTAka/zen-ai-pentest.git
cd zen-ai-pentest

# Create virtual environment (recommended)
python3 -m venv venv
source venv/bin/activate  # Linux/Mac
# or: venv\Scripts\activate  # Windows

# Install dependencies
pip install -r requirements.txt

# Install Nuclei (optional)
# See: https://nuclei.projectdiscovery.io/
```

### Verify Installation

```bash
python zen_ai_pentest.py --help
```

## ⚙️ Configuration

### Basic Configuration

Edit `config.json` to add your API keys:

```json
{
  "backends": {
    "openrouter_api_key": "sk-or-v1-your-key-here",
    "chatgpt_token": "your-chatgpt-session-token",
    "claude_session": "your-claude-session-key"
  },
  "stealth": {
    "delay_min": 1,
    "delay_max": 3,
    "random_user_agent": true
  },
  "output": {
    "save_logs": true,
    "log_level": "INFO",
    "report_format": "markdown"
  }
}
```

## 🚀 Usage

### Interactive Mode

```bash
python zen_ai_pentest.py --interactive
```

### CVE & Ransomware Database Query

```python
from modules.cve_database import CVEDatabase

cve_db = CVEDatabase()

# Search for specific CVE
cve = cve_db.search_cve("CVE-2017-0144")
print(f"{cve.cve_id}: {cve.name} (CVSS: {cve.cvss_score})")

# Check for ransomware
ransomware = cve_db.search_ransomware("WannaCry")
print(f"Decryptable: {ransomware.decryptable}")

# Get IOCs
iocs = cve_db.get_ransomware_iocs("NotPetya")
print(iocs["hashes"])
```

### SQL Injection Testing

```python
from modules.sql_injection_db import SQLInjectionDatabase, DBType, SQLITechnique

sqli_db = SQLInjectionDatabase()

# Get MySQL time-based payloads
payloads = sqli_db.get_payloads(
    db_type=DBType.MYSQL,
    technique=SQLITechnique.BLIND_TIME
)

for payload in payloads:
    print(f"{payload.name}: {payload.payload}")

# Generate WAF bypass variants
variants = sqli_db.generate_waf_bypass_variants("' OR 1=1--")
```

### Nuclei Integration

```python
from modules.nuclei_integration import NucleiIntegration

nuclei = NucleiIntegration(orchestrator)

# Update templates
await nuclei.update_templates()

# Scan target
findings = await nuclei.scan_target(
    target="example.com",
    severity=["critical", "high"],
    tags=["cve", "panel"]
)

# Export results
nuclei.export_results(findings)
```

### Quick Start Examples

#### 1. Target Reconnaissance

```bash
python zen_ai_pentest.py --target example.com --recon
```

#### 2. Analyze Nmap Scan

```bash
# First run nmap
nmap -sV -sC -O example.com -oN scan.txt

# Then analyze with Zen AI
python zen_ai_pentest.py --analyze scan.txt
```

#### 3. Interactive Session

```bash
$ python zen_ai_pentest.py -i

zen-ai> target example.com
[*] Starting Reconnaissance for example.com
[+] Target IP: 93.184.216.34
[+] Attack vectors identified: 5

zen-ai> analyze scan.txt
[+] Found 3 potential vulnerabilities
    [High] Outdated Apache Version
    [Medium] Missing Security Headers
    [Low] Directory Listing Enabled

zen-ai> exploit "CVE-2017-0144" "smb"
[+] Generating exploit suggestions for EternalBlue...
[+] Ransomware using this CVE: WannaCry, NotPetya

zen-ai> report example.com
[+] Markdown report saved: logs/report_example.com_20240129_143022.md
[+] JSON export saved: logs/report_20240129_143022.json
```

## 🔌 CVE & Ransomware Database

### Supported Ransomware Families

| Ransomware | First Seen | Associated CVEs | Decryptable |
|------------|------------|-----------------|-------------|
| **NotPetya** | 2017-06 | CVE-2017-0144/45/46/47/48 | ❌ |
| **WannaCry** | 2017-05 | CVE-2017-0144 | ❌ |
| **Bad Rabbit** | 2017-10 | - | ❌ |
| **Ryuk** | 2018-08 | - | ❌ |
| **Sodinokibi/REvil** | 2019-04 | CVE-2019-2725, CVE-2019-11510 | ✅ |
| **DarkSide** | 2020-08 | - | ✅ |

### Database Features

- **IOCs**: File hashes, registry keys, network indicators
- **Exploit Chains**: Common attack progressions
- **Mitigation**: Specific countermeasures
- **Detection**: SIEM rules and monitoring strategies
- **AI Analysis**: LLM-powered threat assessment

## 💉 SQL Injection Database

### Database Support

- MySQL/MariaDB
- PostgreSQL
- Microsoft SQL Server
- Oracle Database
- SQLite
- MongoDB (NoSQL)

### Techniques Covered

1. **Error-Based** - Extract data via error messages
2. **Union-Based** - Use UNION SELECT for data extraction
3. **Boolean Blind** - True/false inference
4. **Time-Based Blind** - Delay-based extraction
5. **Stacked Queries** - Execute multiple statements
6. **Out-of-Band** - DNS/HTTP exfiltration

### WAF Bypass Features

- URL encoding (single/double)
- Base64 encoding
- Unicode normalization
- Comment injection
- Case variation
- Space alternatives

## 🔍 Nuclei Integration

### Features

- Template management
- Automated scanning
- AI-powered result analysis
- Export to multiple formats
- Severity-based filtering

### Critical CVE Templates Included

- CVE-2017-0144 (EternalBlue)
- CVE-2021-44228 (Log4Shell)
- CVE-2019-11510 (Pulse Secure)
- CVE-2020-1472 (Zerologon)
- CVE-2021-26855 (ProxyLogon)

## 🤖 Multi-Agent System

Inspired by **Clawed/Moltbot**, Zen AI Pentest includes a collaborative multi-agent system where specialized agents work together, share context, and conduct research.

### Agent Roles

| Agent | Role | Responsibility |
|-------|------|---------------|
| **ResearchBot** | Researcher | Gathers CVE data, performs reconnaissance |
| **AnalysisBot** | Analyst | Identifies patterns, correlates findings |
| **ExploitBot** | Exploit | Develops payloads, suggests techniques |

### Key Features

- **Inter-Agent Messaging** - Agents can send messages to each other (broadcast, role-based, direct)
- **Context Sharing** - Shared workspace for all findings and research
- **Collaborative Research** - Multiple agents work on the same topic simultaneously
- **Conversation Facilitation** - Agents can have multi-round discussions
- **Distributed Workload** - Prevents the main pentest AI from being overwhelmed

### Using the Agent System

```python
from agents.integration import AgentSystemIntegration

# Initialize
agents = AgentSystemIntegration(zen_orchestrator)
await agents.initialize()

# Start collaborative research
thread_id = await agents.conduct_research(
    topic="WordPress CVEs",
    pentest_context={"target": "example.com"}
)

# Let agents analyze together
results = await agents.analyze_target("example.com", findings)

# Facilitate agent discussion
messages = await agents.facilitate_discussion(
    topic="Attack vectors for CVE-2017-0144",
    rounds=3
)
```

### Agent CLI

```bash
# Start the agent CLI
python agents/cli.py

# Available commands:
agents> research WordPress vulnerabilities
agents> analyze example.com
agents> discuss Ransomware IOCs
agents> status
```

## 🔌 API Backends

### Backend Priority System

| Priority | Backend | Authentication | Rate Limit | Best For |
|----------|---------|---------------|------------|----------|
| 1 | DuckDuckGo AI | None | ~50/day | Quick queries, recon |
| 2 | OpenRouter | API Key | Varies by model | Code analysis |
| 3 | ChatGPT Direct | Session Token | 40/3h | Complex reasoning |
| 3 | Claude Direct | Session Key | Varies | Long-form analysis |

### Quality Levels

```python
from core.orchestrator import QualityLevel

# Low quality - fast, free (DuckDuckGo)
result = await orchestrator.process(prompt, QualityLevel.LOW)

# Medium quality - OpenRouter free tier
result = await orchestrator.process(prompt, QualityLevel.MEDIUM)

# High quality - Direct APIs
result = await orchestrator.process(prompt, QualityLevel.HIGH)
```

## 🎯 WordPress Nuclei Templates

Pre-built Nuclei templates for WordPress penetration testing:

| Template | Severity | Description |
|----------|----------|-------------|
| `wp-login-brute.yaml` | Medium | Detects wp-login.php and brute force potential |
| `wp-xmlrpc-pingback.yaml` | High | XML-RPC pingback amplification vulnerability |
| `wp-users-api.yaml` | Medium | REST API user enumeration |
| `wp-debug-log.yaml` | High | Debug.log file exposure |
| `wp-config-backup.yaml` | Critical | wp-config.php backup file exposure |

### Usage

```python
from modules.nuclei_integration import NucleiIntegration

nuclei = NucleiIntegration(orchestrator)

# Scan with WordPress templates
findings = await nuclei.scan_target(
    target="wordpress-site.com",
    templates=["data/nuclei_templates/wordpress/wp-config-backup.yaml"]
)
```

## 📁 Project Structure

```
zen-ai-pentest/
├── core/                       # Core orchestrator
├── backends/                   # LLM backends (4x)
├── modules/                    # Penetration Testing (7x)
│   ├── recon.py
│   ├── vuln_scanner.py
│   ├── exploit_assist.py
│   ├── report_gen.py
│   ├── nuclei_integration.py   # NEW
│   ├── sql_injection_db.py     # NEW
│   └── cve_database.py         # NEW
├── agents/                     # NEW: Multi-Agent System
│   ├── agent_base.py
│   ├── agent_orchestrator.py
│   ├── research_agent.py
│   ├── analysis_agent.py
│   ├── exploit_agent.py
│   ├── integration.py
│   └── cli.py
├── data/                       # NEW: Databases
│   ├── cve_db/
│   │   └── ransomware_cves.json
│   ├── nuclei_templates/
│   │   └── wordpress/          # NEW: WordPress templates
│   └── payloads/
├── utils/                      # Helper utilities
├── examples/                   # Example scripts
├── sessions/                   # Session storage
├── logs/                       # Reports & logs
├── tests/                      # Unit tests
├── zen_ai_pentest.py          # Main entry point
├── README.md
├── LICENSE
├── setup.py
└── requirements.txt
```

## 🔧 Troubleshooting

### Windows Python 3.13+ AsyncIO Errors

If you see errors like:
```
Exception in callback _ProactorBasePipeTransport._call_connection_lost()
```

**This is a known Python 3.13 issue on Windows.** The tool includes automatic patches, but if you still see these errors:

1. **They are harmless** - The tool continues to work correctly
2. **To suppress completely**, set environment variable:
   ```powershell
   $env:PYTHONWARNINGS="ignore"
   python zen_ai_pentest.py
   ```

3. **Alternative**: Use Python 3.11 or 3.12 where this issue doesn't occur

### Import Errors

If you get `ModuleNotFoundError`:
```bash
# Ensure you're in the project directory
cd zen-ai-pentest

# Reinstall dependencies
pip install -r requirements.txt
```

### Connection Errors

If backends fail to connect:
1. Check your internet connection
2. Verify API keys in `config.json`
3. DuckDuckGo backend requires no authentication and is most reliable
4. Try with just DuckDuckGo first:
   ```python
   from core.orchestrator import ZenOrchestrator
   from backends.duckduckgo import DuckDuckGoBackend
   
   orch = ZenOrchestrator()
   async with DuckDuckGoBackend() as ddg:
       orch.add_backend(ddg)
       result = await orch.process("test")
   ```

## 👥 Contributors

### Core Team

**SHAdd0WTAka** - Project Lead, Lead Developer  
[@SHAdd0WTAka](https://github.com/SHAdd0WTAka)

**Kimi AI** (Moonshot AI) - AI Assistant, Co-Developer  
Research, documentation, PostScanAgent implementation, CI/CD workflows

> "Nur wer Schwert und Schild besitzt, kann sich wirklich als Pentester beweisen."

See [CONTRIBUTORS.md](CONTRIBUTORS.md) for full contributor list.

## 🤝 Contributing

Contributions are welcome! Please follow these guidelines:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Development Setup

```bash
pip install -r requirements.txt
pip install pytest pytest-asyncio black pylint

# Run tests
pytest tests/

# Format code
black .
```

## ⚖️ Legal Disclaimer

This tool is intended for authorized security testing only. Users are responsible for complying with all applicable laws and regulations. The authors assume no liability for misuse or damage caused by this tool.

**Only use Zen AI Pentest on systems you have explicit written permission to test.**

The CVE and exploit information provided is for educational and defensive purposes only.

## 📜 License

MIT License - see [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **Moonshot AI** for Kimi AI assistance in development and documentation
- DuckDuckGo for their free AI chat API
- OpenRouter for unified LLM access
- ProjectDiscovery for Nuclei scanner
- The security community for continuous research

## 📧 Contact

**Author:** SHAdd0WTAka

For questions, issues, or contributions, please use GitHub issues.

---

<div align="center">

**[⬆ Back to Top](#-zen-ai-pentest)**

⭐ Star this repository if you find it helpful! ⭐

</div>
