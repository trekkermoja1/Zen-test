"""
Multi-Agent Collaboration System for Zen AI Pentest
Inspired by Clawed/Moltbot architecture
Agents can communicate, share context, and coordinate research
Author: SHAdd0WTAka
"""

from .agent_base import BaseAgent, AgentRole, AgentMessage
from .agent_orchestrator import AgentOrchestrator
from .research_agent import ResearchAgent
from .exploit_agent import ExploitAgent
from .analysis_agent import AnalysisAgent

__all__ = [
    'BaseAgent',
    'AgentRole', 
    'AgentMessage',
    'AgentOrchestrator',
    'ResearchAgent',
    'ExploitAgent',
    'AnalysisAgent'
]
