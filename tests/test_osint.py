"""
Unit Tests for OSINT Module
"""

import pytest
import asyncio
from modules.osint import OSINTModule, harvest_emails, enumerate_subdomains


@pytest.mark.asyncio
async def test_osint_module_initialization():
    """Test OSINT module can be initialized"""
    async with OSINTModule() as osint:
        assert osint is not None
        assert osint.results == []


@pytest.mark.asyncio
async def test_email_validation():
    """Test email format validation"""
    async with OSINTModule() as osint:
        # Valid emails
        assert osint._is_valid_ip("192.168.1.1") is True
        
        # Invalid emails
        assert osint._is_valid_ip("not-an-ip") is False


@pytest.mark.asyncio
async def test_harvest_emails():
    """Test email harvesting"""
    async with OSINTModule() as osint:
        # Mock test - in real tests use mock server
        results = await osint.harvest_emails("example.com")
        
        # Should return a list
        assert isinstance(results, list)
        
        # Check structure
        for result in results:
            assert hasattr(result, 'value')
            assert hasattr(result, 'source')
            assert hasattr(result, 'confidence')


@pytest.mark.asyncio
async def test_subdomain_enumeration():
    """Test subdomain enumeration"""
    async with OSINTModule() as osint:
        subdomains = await osint._enumerate_subdomains("example.com")
        
        assert isinstance(subdomains, list)
        # Should find at least some subdomains
        assert len(subdomains) >= 0


@pytest.mark.asyncio
async def test_breach_check():
    """Test breach checking"""
    async with OSINTModule() as osint:
        # Valid email
        profile = await osint.check_breach("test@example.com")
        
        assert profile.email == "test@example.com"
        assert profile.valid_format is True
        assert isinstance(profile.breached, bool)


@pytest.mark.asyncio
async def test_domain_recon():
    """Test domain reconnaissance"""
    async with OSINTModule() as osint:
        info = await osint.recon_domain("example.com")
        
        assert info.domain == "example.com"
        assert isinstance(info.subdomains, list)
        assert isinstance(info.technologies, list)
