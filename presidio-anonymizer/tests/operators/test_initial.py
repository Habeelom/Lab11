"""Tests for the Initial operator."""
import pytest
from presidio_anonymizer.operators import Initial


def test_initial_transforms_regular_names():
    """Test that initial operator transforms names correctly."""
    operator = Initial()
    
    # Test "John Smith" -> "J. S."
    result = operator.operate("John Smith", {})
    assert result == "J. S."
    
    # Test lowercase "john smith" -> "J. S."
    result = operator.operate("john smith", {})
    assert result == "J. S."