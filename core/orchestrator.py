#!/usr/bin/env python3
"""
Zen AI Hybrid Orchestrator
Multi-LLM Routing System with Penetration Testing Capabilities
Author: SHAdd0WTAka
"""

import asyncio
import aiohttp
import json
import random
import traceback
import sys
import os
from abc import ABC, abstractmethod
from typing import Optional, Dict, Any, List
from dataclasses import dataclass
from enum import Enum
import logging
from datetime import datetime

# Apply Windows/asyncio fixes before any other imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils.async_fixes import apply_windows_async_fixes, safe_close_session
apply_windows_async_fixes()

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('logs/zen_ai.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger("ZenAI")


class QualityLevel(Enum):
    """Quality levels for LLM responses"""
    LOW = "low"        # Fast, free (DDG)
    MEDIUM = "medium"  # OpenRouter Free Tier
    HIGH = "high"      # Direct API (ChatGPT/Claude Web)


@dataclass
class LLMResponse:
    """Standardized LLM response"""
    content: str
    source: str
    latency: float
    quality: QualityLevel
    metadata: Dict = None


class BaseBackend(ABC):
    """Abstract base class for LLM backends"""
    
    def __init__(self, name: str, priority: int):
        self.name = name
        self.priority = priority
        self.session: Optional[aiohttp.ClientSession] = None
        
    async def __aenter__(self):
        self.session = aiohttp.ClientSession()
        return self
        
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        if self.session:
            await safe_close_session(self.session)
            
    @abstractmethod
    async def chat(self, prompt: str, context: str = "") -> Optional[str]:
        """Send prompt to backend and return response"""
        pass
        
    async def health_check(self) -> bool:
        """Check if backend is available"""
        return True


class ZenOrchestrator:
    """
    Central orchestrator for multi-LLM management
    Routes requests to appropriate backends based on quality requirements
    """
    
    def __init__(self):
        self.backends: List[BaseBackend] = []
        self.results_cache = {}
        self.request_count = 0
        
    def add_backend(self, backend: BaseBackend):
        """Register a new backend"""
        self.backends.append(backend)
        # Sort by priority (lowest first = faster/free)
        self.backends.sort(key=lambda x: x.priority)
        logger.info(f"[Zen] Backend '{backend.name}' registered with priority {backend.priority}")
        
    async def process(self, prompt: str, required_quality: QualityLevel = QualityLevel.MEDIUM) -> LLMResponse:
        """
        Process a prompt through available backends
        Tries backends in priority order with automatic fallback
        """
        self.request_count += 1
        start_time = asyncio.get_event_loop().time()
        
        logger.info(f"[Zen] Request #{self.request_count} | Quality: {required_quality.value}")
        
        # Filter candidates based on quality requirement
        if required_quality == QualityLevel.LOW:
            candidates = [b for b in self.backends if b.priority == 1]
        elif required_quality == QualityLevel.MEDIUM:
            candidates = [b for b in self.backends if b.priority <= 2]
        else:
            candidates = self.backends
            
        # Try sequentially (faster than parallel for different tiers)
        for backend in candidates:
            logger.info(f"[Zen] Trying {backend.name}...")
            
            try:
                result = await backend.chat(prompt)
                
                if result and len(result) > 10:
                    latency = asyncio.get_event_loop().time() - start_time
                    
                    quality = QualityLevel.HIGH if backend.priority == 3 else \
                             QualityLevel.MEDIUM if backend.priority == 2 else \
                             QualityLevel.LOW
                             
                    logger.info(f"[Zen] Success from {backend.name} in {latency:.2f}s")
                    
                    return LLMResponse(
                        content=result,
                        source=backend.name,
                        latency=latency,
                        quality=quality,
                        metadata={"model": getattr(backend, "current_model", "unknown")}
                    )
                    
            except Exception as e:
                logger.error(f"[Zen] Backend {backend.name} failed: {e}")
                continue
                
        # Complete failure
        logger.error("[Zen] All backends failed")
        return LLMResponse(
            content="All backends failed. Check logs.",
            source="None",
            latency=0,
            quality=QualityLevel.LOW
        )
        
    async def parallel_consensus(self, prompt: str) -> Dict[str, Any]:
        """
        For critical tasks: Query multiple backends simultaneously
        Returns consensus and alternative responses
        """
        logger.info("[Zen] Parallel consensus mode activated")
        
        tasks = []
        for backend in self.backends[:2]:  # Top 2 (DDG + OpenRouter)
            tasks.append(backend.chat(prompt))
            
        results = await asyncio.gather(*tasks, return_exceptions=True)
        
        valid = []
        for backend, result in zip(self.backends[:2], results):
            if isinstance(result, str) and len(result) > 50:
                valid.append({"source": backend.name, "content": result})
                
        return {
            "responses": valid,
            "consensus": valid[0] if valid else None,
            "alternative": valid[1] if len(valid) > 1 else None
        }
        
    def get_stats(self) -> Dict:
        """Get orchestrator statistics"""
        return {
            "backends_registered": len(self.backends),
            "backends": [b.name for b in self.backends],
            "requests_processed": self.request_count
        }
