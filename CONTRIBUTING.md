# Contributing to Zen AI Pentest

Thank you for your interest in contributing to Zen AI Pentest! This document provides guidelines and instructions for contributing.

## Code of Conduct

This project and everyone participating in it is governed by our Code of Conduct. By participating, you are expected to uphold this code.

## How Can I Contribute?

### Reporting Bugs

Before creating bug reports, please check the existing issues to avoid duplicates. When you create a bug report, include:

- **Use a clear descriptive title**
- **Describe the exact steps to reproduce**
- **Provide specific examples** (commands, configs)
- **Describe the behavior you observed**
- **Explain which behavior you expected**
- **Include system information** (OS, Python version)

### Suggesting Enhancements

Enhancement suggestions are tracked as GitHub issues. When creating an enhancement suggestion:

- **Use a clear descriptive title**
- **Provide a step-by-step description**
- **Provide specific examples**
- **Explain why this enhancement would be useful**

### Adding CVEs or Payloads

We welcome additions to our databases!

#### Adding a CVE:
1. Edit `data/cve_database.json`
2. Follow the existing JSON structure
3. Include all required fields (CVE ID, description, CVSS, etc.)
4. Verify JSON validity: `python -m json.tool data/cve_database.json`

#### Adding SQL Injection Payloads:
1. Edit the appropriate file in `data/sql_injection/`
2. Include description and expected behavior
3. Test with relevant database type
4. Document any special requirements

#### Adding Ransomware IOCs:
1. Edit `data/ransomware_families.json`
2. Include comprehensive IOCs (file extensions, registry keys, URLs)
3. Add MITRE ATT&CK mappings
4. Include financial damage estimates if available

### Pull Requests

1. Fork the repository
2. Create a new branch: `git checkout -b feature/my-feature`
3. Make your changes
4. Run tests and demos
5. Commit your changes: `git commit -am 'Add new feature'`
6. Push to the branch: `git push origin feature/my-feature`
7. Submit a pull request

## Development Setup

### Prerequisites

- Python 3.9 or higher
- Git

### Setting Up

```bash
# Clone the repository
git clone https://github.com/SHAdd0WTAka/zen-ai-pentest.git
cd zen-ai-pentest

# Create virtual environment
python -m venv venv

# Activate (Windows)
venv\Scripts\activate

# Activate (Linux/macOS)
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
pip install -r requirements-dev.txt  # Development dependencies
```

### Running Tests

```bash
# Run all demos
python examples/cve_and_ransomware_demo.py
python examples/multi_agent_demo.py

# Run tests (if available)
pytest tests/

# Lint code
flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
black --check .
```

## Style Guidelines

### Python Code Style

- Follow PEP 8
- Use meaningful variable names
- Add docstrings to functions and classes
- Keep functions focused and small
- Maximum line length: 127 characters

### Documentation

- Update README.md if adding features
- Add docstrings for new functions
- Update relevant .md files in docs/
- Include examples in documentation

### Commit Messages

- Use the present tense ("Add feature" not "Added feature")
- Use the imperative mood ("Move cursor to..." not "Moves cursor to...")
- Limit the first line to 72 characters or less
- Reference issues and pull requests liberally after the first line

Example:
```
Add support for PostgreSQL injection payloads

- Add 5 new PostgreSQL-specific payloads
- Update SQLi database documentation
- Fixes #123
```

## Security Considerations

This is a penetration testing framework. When contributing:

- **Never** include real API keys or credentials
- **Never** include actual exploited system data
- **Always** validate inputs to prevent injection
- **Always** use safe subprocess execution
- **Test** thoroughly before submitting

## Database Contributions

### CVE Database Structure

```json
{
  "CVE-2021-44228": {
    "description": "Log4j RCE vulnerability",
    "cvss_score": 10.0,
    "cvss_vector": "CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H",
    "affected_systems": ["Apache Log4j 2.0-beta9 to 2.14.1"],
    "ransomware_associations": ["Khonsari", "Conti"],
    "exploit_available": true,
    "poc_available": true,
    "mitre_techniques": ["T1190", "T1059"],
    "ioc_file_hashes": [],
    "ioc_registry_keys": [],
    "ioc_urls": [],
    "ioc_ips": [],
    "remediation": "Update to Log4j 2.15.0 or later"
  }
}
```

### SQL Injection Payload Structure

```json
{
  "payloads": [
    {
      "name": "MySQL Version Detection",
      "payload": "' UNION SELECT @@version--",
      "description": "Extracts MySQL version",
      "context": "error_based",
      "database_type": "mysql",
      "waf_bypass": false
    }
  ]
}
```

## Review Process

All submissions require review before being merged:

1. Automated checks must pass (CI/CD)
2. Code review by maintainers
3. Security review for sensitive changes
4. Documentation review

## Recognition

Contributors will be recognized in our README.md Contributors section.

## Questions?

Feel free to:
- Open an issue with the `question` label
- Join discussions in existing issues
- Contact maintainers

Thank you for contributing to Zen AI Pentest!
