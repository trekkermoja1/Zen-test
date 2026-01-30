"""
Unit Tests for Ransomware Database
"""

import pytest
from core.database import get_ransomware_db


def test_ransomware_db_loading():
    """Test ransomware database loads correctly"""
    db = get_ransomware_db()
    
    # Should be a list of ransomware families
    assert isinstance(db, list)
    assert len(db) > 0


def test_ransomware_family_structure():
    """Test ransomware family data structure"""
    db = get_ransomware_db()
    
    for family in db:
        # Required fields
        assert "name" in family
        assert "family" in family
        assert "first_seen" in family
        assert "extensions" in family
        
        # Check data types
        assert isinstance(family["name"], str)
        assert isinstance(family["extensions"], list)


def test_specific_ransomware_families():
    """Test specific ransomware families exist"""
    db = get_ransomware_db()
    
    family_names = [f["name"].lower() for f in db]
    
    # Check for common families
    common_families = [
        "wannacry", "petya", "notpetya", "ryuk", 
        "revil", "maze", "conti"
    ]
    
    # At least some should be present
    found = [f for f in common_families if any(f in name for name in family_names)]
    assert len(found) > 0, "No common ransomware families found"
