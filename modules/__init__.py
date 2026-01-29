"""
Penetration Testing Modules for Zen AI
"""

from .recon import ReconModule
from .vuln_scanner import VulnScannerModule
from .exploit_assist import ExploitAssistModule
from .report_gen import ReportGenerator
from .nuclei_integration import NucleiIntegration, NucleiTemplateManager
from .sql_injection_db import SQLInjectionDatabase, SQLPayload, SQLITechnique, DBType
from .cve_database import CVEDatabase, CVEEntry, RansomwareEntry

__all__ = [
    'ReconModule',
    'VulnScannerModule',
    'ExploitAssistModule',
    'ReportGenerator',
    'NucleiIntegration',
    'NucleiTemplateManager',
    'SQLInjectionDatabase',
    'SQLPayload',
    'SQLITechnique',
    'DBType',
    'CVEDatabase',
    'CVEEntry',
    'RansomwareEntry'
]
