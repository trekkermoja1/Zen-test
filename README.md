# 🛡️ Zen AI Pentest

**AI-Powered Multi-LLM Penetration Testing Intelligence System**

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Author](https://img.shields.io/badge/Author-SHADDOWTAKA-red.svg)](#)

> ⚠️ **DISCLAIMER**: This tool is for authorized security testing only. Always obtain proper permission before testing any systems you do not own.

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Architecture](#architecture)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Modules](#modules)
- [API Backends](#api-backends)
- [Contributing](#contributing)

## 🎯 Overview

Zen AI Pentest is an advanced penetration testing framework that leverages multiple Large Language Models (LLMs) to assist security professionals in reconnaissance, vulnerability analysis, exploit assistance, and report generation. The system intelligently routes requests across free and authenticated LLM backends to maximize efficiency and minimize API costs.

### Key Highlights

- 🔗 **Multi-LLM Integration** - Seamlessly switches between DuckDuckGo AI, OpenRouter, ChatGPT, and Claude
- 🧠 **AI-Powered Analysis** - Intelligent vulnerability detection and exploit suggestion
- 📊 **Automated Reporting** - Generate professional pentest reports in multiple formats
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
| Report Generation | Professional markdown, JSON, CSV, and HTML reports | ✅ |
| Session Management | Persistent sessions for authenticated backends | ✅ |
| Stealth Mode | Random delays, user-agent rotation, and evasion techniques | ✅ |
| Interactive CLI | User-friendly command-line interface | ✅ |

### Penetration Testing Modules

#### 1. 🔍 Reconnaissance Module (`modules/recon.py`)
- DNS enumeration and analysis
- Subdomain discovery
- WHOIS information gathering
- Nmap command optimization
- Attack vector identification via LLM

#### 2. 🐛 Vulnerability Scanner (`modules/vuln_scanner.py`)
- Nmap output analysis
- HTTP security header assessment
- Web page content analysis
- CVE database lookups
- SSL/TLS configuration review
- Severity-based prioritization

#### 3. 💥 Exploit Assistance (`modules/exploit_assist.py`)
- Exploit technique suggestions
- SQL injection payload generation
- XSS proof-of-concept creation
- Post-exploitation guidance
- Security control bypass techniques

#### 4. 📄 Report Generator (`modules/report_gen.py`)
- Executive summaries
- Technical findings reports
- Remediation roadmaps
- Compliance mapping (NIST, ISO27001, etc.)
- Multiple export formats

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    Zen AI Pentest                           │
├─────────────────────────────────────────────────────────────┤
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────────────┐  │
│  │   Recon     │  │  Vuln Scan  │  │  Exploit Assist     │  │
│  │   Module    │  │   Module    │  │     Module          │  │
│  └──────┬──────┘  └──────┬──────┘  └──────────┬──────────┘  │
│         └─────────────────┼────────────────────┘             │
│                           │                                  │
│                    ┌──────┴──────┐                          │
│                    │ ZenOrchestrator│                        │
│                    │   (Router)     │                        │
│                    └──────┬──────┘                          │
│                           │                                  │
│         ┌─────────────────┼─────────────────┐               │
│         │                 │                 │                │
│    ┌────┴────┐      ┌────┴────┐      ┌────┴────┐           │
│    │  DDG    │      │OpenRouter│      │ Direct  │           │
│    │ (Free)  │      │(Free Tier)│      │  APIs   │           │
│    └─────────┘      └─────────┘      └─────────┘           │
└─────────────────────────────────────────────────────────────┘
```

## 📦 Installation

### Prerequisites

- Python 3.8 or higher
- pip or pip3

### Quick Install

```bash
# Clone the repository
git clone https://github.com/SHADDOWTAKA/zen-ai-pentest.git
cd zen-ai-pentest

# Create virtual environment (recommended)
python3 -m venv venv
source venv/bin/activate  # Linux/Mac
# or: venv\Scripts\activate  # Windows

# Install dependencies
pip install -r requirements.txt
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

### Getting API Tokens

#### DuckDuckGo AI
- ✅ No configuration required - works out of the box
- Limited to ~50-100 requests per day

#### OpenRouter (Recommended)
1. Visit [openrouter.ai](https://openrouter.ai)
2. Create a free account
3. Generate an API key
4. Add to `config.json`

#### ChatGPT Direct (Optional)
1. Login to ChatGPT in your browser
2. Open DevTools (F12) → Application → Cookies
3. Copy `__Secure-next-auth.session-token`
4. Paste into `config.json`
5. Token lasts 2-4 weeks

#### Claude Direct (Optional)
1. Login to Claude.ai in your browser
2. Open DevTools → Application → Cookies
3. Copy `sessionKey` cookie
4. Paste into `config.json`

## 🚀 Usage

### Interactive Mode

```bash
python zen_ai_pentest.py --interactive
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

zen-ai> exploit "Outdated Apache" "apache"
[+] Generating exploit suggestions...

zen-ai> report example.com
[+] Markdown report saved: logs/report_example.com_20240129_143022.md
[+] JSON export saved: logs/report_20240129_143022.json
```

### Python API Usage

```python
import asyncio
from zen_ai_pentest import ZenAIPentest

async def main():
    # Initialize app
    app = ZenAIPentest(config_path="config.json")
    await app.initialize_backends()
    
    # Run reconnaissance
    recon_results = await app.run_recon("example.com")
    
    # Analyze findings
    vulns = await app.vuln_scanner.analyze_nmap_output(nmap_data)
    
    # Generate report
    report = await app.generate_report("example.com")
    
asyncio.run(main())
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

## 📁 Project Structure

```
zen-ai-pentest/
├── core/
│   ├── __init__.py
│   └── orchestrator.py          # Main routing logic
├── backends/
│   ├── __init__.py
│   ├── duckduckgo.py           # DDG AI backend
│   ├── openrouter.py           # OpenRouter backend
│   ├── chatgpt_direct.py       # ChatGPT API
│   └── claude_direct.py        # Claude API
├── modules/
│   ├── __init__.py
│   ├── recon.py                # Reconnaissance
│   ├── vuln_scanner.py         # Vulnerability analysis
│   ├── exploit_assist.py       # Exploit suggestions
│   └── report_gen.py           # Report generation
├── utils/
│   ├── __init__.py
│   ├── helpers.py              # Utility functions
│   └── stealth.py              # Stealth utilities
├── sessions/                    # Session storage
├── logs/                        # Log files and reports
├── tests/                       # Unit tests
├── zen_ai_pentest.py           # Main entry point
├── config.json                 # Configuration
├── requirements.txt            # Dependencies
└── README.md                   # This file
```

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

## 📜 License

MIT License - see [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- DuckDuckGo for their free AI chat API
- OpenRouter for unified LLM access
- The security community for continuous research

## 📧 Contact

**Author:** SHADDOWTAKA

For questions, issues, or contributions, please use GitHub issues.

---

<div align="center">

**[⬆ Back to Top](#-zen-ai-pentest)**

⭐ Star this repository if you find it helpful! ⭐

</div>
