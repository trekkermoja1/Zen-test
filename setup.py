#!/usr/bin/env python3
"""
Setup script for Zen AI Pentest
Author: SHAdd0WTAka
"""

from setuptools import find_packages, setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [
        line.strip() for line in fh if line.strip() and not line.startswith("#")
    ]

setup(
    name="zen-ai-pentest",
    version="1.0.0",
    author="SHAdd0WTAka",
    author_email="SHAdd0WTAka@example.com",
    description="Multi-LLM Penetration Testing Intelligence System",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/SHAdd0WTAka/zen-ai-pentest",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Information Technology",
        "Topic :: Security",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
    python_requires=">=3.8",
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "zen-ai=zen_ai_pentest:main",
        ],
    },
)
