"""
Zen Shield - Security Sanitization Module

Protects sensitive data from leaking to external LLMs by:
- Automatic secret detection and masking
- Context compression to reduce costs
- Prompt injection detection
- Local processing with optional small LLM
"""

from .schemas import SanitizerRequest, SanitizerResponse, RiskLevel
from .sanitizer import ZenSanitizer
from .filters.secrets import SecretScrubber
from .filters.compress import ContextCompressor
from .circuit_breaker import CircuitBreaker

__version__ = "1.0.0"
__all__ = [
    "ZenSanitizer",
    "SanitizerRequest",
    "SanitizerResponse",
    "RiskLevel",
    "SecretScrubber",
    "ContextCompressor",
    "CircuitBreaker",
]
