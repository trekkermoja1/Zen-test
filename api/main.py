"""
Zen AI Pentest - FastAPI Application

Main API entry point providing:
- RESTful endpoints for pentest operations
- WebSocket support for real-time updates
- Authentication and authorization
- Rate limiting
- Automatic API documentation (Swagger/OpenAPI)
"""

import asyncio
import logging
from contextlib import asynccontextmanager
from typing import Optional

from fastapi import FastAPI, Request, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.gzip import GZipMiddleware
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles

# Import routers
from api.routes import (
    auth,
    scans,
    findings,
    reports,
    agents,
    vpn,
    system,
    websocket,
    osint
)
from api.core.config import settings
from api.core.database import close_db, init_db
from api.core.cache import close_cache, init_cache
from api.core.middleware import (
    RateLimitMiddleware,
    LoggingMiddleware,
    SecurityHeadersMiddleware
)

logger = logging.getLogger("ZenAI.API")


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Application lifespan manager."""
    logger.info("Starting Zen AI Pentest API...")
    
    await init_db()
    logger.info("Database initialized")
    
    await init_cache()
    logger.info("Cache initialized")
    
    from api.core.agents import agent_manager
    await agent_manager.start()
    logger.info("Agent manager started")
    
    logger.info("API startup complete")
    
    yield
    
    logger.info("Shutting down API...")
    await agent_manager.stop()
    await close_cache()
    await close_db()
    logger.info("API shutdown complete")


def create_app() -> FastAPI:
    """Create and configure FastAPI application."""
    app = FastAPI(
        title="Zen AI Pentest API",
        description="AI-Powered Penetration Testing Framework API",
        version="1.0.0",
        docs_url="/docs",
        redoc_url="/redoc",
        openapi_url="/openapi.json",
        lifespan=lifespan
    )
    
    # Middleware
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.CORS_ORIGINS,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    app.add_middleware(GZipMiddleware, minimum_size=1000)
    app.add_middleware(SecurityHeadersMiddleware)
    app.add_middleware(LoggingMiddleware)
    app.add_middleware(RateLimitMiddleware)
    
    # Routers
    app.include_router(auth.router, prefix="/api/v1/auth", tags=["Authentication"])
    app.include_router(scans.router, prefix="/api/v1/scans", tags=["Scans"])
    app.include_router(findings.router, prefix="/api/v1/findings", tags=["Findings"])
    app.include_router(reports.router, prefix="/api/v1/reports", tags=["Reports"])
    app.include_router(agents.router, prefix="/api/v1/agents", tags=["Agents"])
    app.include_router(vpn.router, prefix="/api/v1/vpn", tags=["VPN"])
    app.include_router(osint.router, prefix="/api/v1/osint", tags=["OSINT"])
    app.include_router(system.router, prefix="/api/v1/system", tags=["System"])
    app.include_router(websocket.router, prefix="/ws", tags=["WebSocket"])
    
    # Static files
    app.mount("/static", StaticFiles(directory="reports"), name="static")
    
    @app.exception_handler(Exception)
    async def global_exception_handler(request: Request, exc: Exception):
        logger.error(f"Unhandled exception: {exc}", exc_info=True)
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={"error": "Internal server error", "message": str(exc)}
        )
    
    @app.get("/", tags=["Root"])
    async def root():
        return {
            "name": "Zen AI Pentest API",
            "version": "1.0.0",
            "status": "operational",
            "documentation": "/docs",
            "health": "/health"
        }
    
    @app.get("/health", tags=["Health"])
    async def health_check():
        return {
            "status": "healthy",
            "version": "1.0.0",
            "services": {
                "database": "connected",
                "cache": "connected",
                "agents": "running"
            }
        }
    
    return app


app = create_app()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("api.main:app", host="0.0.0.0", port=8080, reload=True)
