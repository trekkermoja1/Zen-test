"""
LLM Backends for Zen AI
Supports multiple free and authenticated LLM providers
"""

from .duckduckgo import DuckDuckGoBackend
from .openrouter import OpenRouterBackend
from .chatgpt_direct import ChatGPTDirectBackend
from .claude_direct import ClaudeDirectBackend

__all__ = [
    'DuckDuckGoBackend',
    'OpenRouterBackend', 
    'ChatGPTDirectBackend',
    'ClaudeDirectBackend'
]
