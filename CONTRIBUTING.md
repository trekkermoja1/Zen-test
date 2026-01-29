# Contributing to Zen AI Pentest

Thank you for your interest in contributing to Zen AI Pentest! This document provides guidelines and instructions for contributing.

## 🚀 Getting Started

### Setting Up Development Environment

1. Fork the repository
2. Clone your fork:
```bash
git clone https://github.com/YOUR_USERNAME/zen-ai-pentest.git
cd zen-ai-pentest
```

3. Create a virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

4. Install development dependencies:
```bash
pip install -r requirements.txt
pip install pytest pytest-asyncio black pylint flake8
```

## 📝 Code Style

- Follow PEP 8 style guidelines
- Use `black` for code formatting:
  ```bash
  black .
  ```
- Run `pylint` for code quality checks:
  ```bash
  pylint core/ backends/ modules/ utils/
  ```

## 🧪 Testing

- Write tests for new features
- Run tests before submitting:
  ```bash
  pytest tests/ -v
  ```

## 🔄 Submitting Changes

1. Create a new branch:
```bash
git checkout -b feature/your-feature-name
```

2. Make your changes and commit:
```bash
git add .
git commit -m "Add feature: description"
```

3. Push to your fork:
```bash
git push origin feature/your-feature-name
```

4. Create a Pull Request on GitHub

## 🏷️ Commit Message Guidelines

- Use present tense ("Add feature" not "Added feature")
- Use imperative mood ("Move cursor to..." not "Moves cursor to...")
- Limit first line to 72 characters
- Reference issues and PRs where appropriate

## 🛡️ Security

- Never commit API keys or session tokens
- Use environment variables for sensitive data
- Follow responsible disclosure for security issues

## 📋 Code Review Process

1. All submissions require review
2. Changes must pass CI checks
3. Maintainers will provide feedback
4. Approved PRs will be merged

## 🐛 Reporting Bugs

Use GitHub Issues with the following template:

```
**Description:**
Clear description of the bug

**Steps to Reproduce:**
1. Step one
2. Step two

**Expected Behavior:**
What should happen

**Actual Behavior:**
What actually happens

**Environment:**
- OS: [e.g. Ubuntu 20.04]
- Python version: [e.g. 3.10]
- Version: [e.g. 1.0.0]
```

## 💡 Feature Requests

Use GitHub Issues with label `enhancement` and include:
- Use case description
- Proposed solution
- Alternative solutions considered

## 📜 License

By contributing, you agree that your contributions will be licensed under the MIT License.

## ❓ Questions?

- Open a GitHub Discussion
- Contact: SHAdd0WTAka

Thank you for contributing! 🎉
