"""
Setup script for Zen AI Pentest
"""

from setuptools import setup, find_packages
from pathlib import Path

# Read README
readme_file = Path(__file__).parent / "README.md"
long_description = readme_file.read_text(encoding="utf-8") if readme_file.exists() else ""

# Read requirements
requirements_file = Path(__file__).parent / "requirements.txt"
requirements = []
if requirements_file.exists():
    with open(requirements_file) as f:
        requirements = [
            line.strip() 
            for line in f 
            if line.strip() and not line.startswith("#") and not line.startswith("-")
        ]

setup(
    name="zen-ai-pentest",
    version="1.0.0",
    author="SHAdd0WTAka",
    author_email="shaddowtaka@example.com",
    description="AI-Powered Multi-LLM Penetration Testing Framework",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/SHAdd0WTAka/pentest-ai",
    packages=find_packages(exclude=["tests", "tests.*", "docs", "examples"]),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Information Technology",
        "Topic :: Security",
        "Topic :: Security :: Penetration Testing",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
    python_requires=">=3.9",
    install_requires=requirements,
    extras_require={
        "dev": [
            "pytest>=7.0.0",
            "pytest-asyncio>=0.21.0",
            "black>=23.0.0",
            "pylint>=2.17.0",
            "mypy>=1.7.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "zen-ai-pentest=zen_ai_pentest:main",
            "zen-pentest=zen_ai_pentest:main",
        ],
    },
    include_package_data=True,
    package_data={
        "": ["*.json", "*.yaml", "*.txt", "*.md"],
    },
    zip_safe=False,
)
