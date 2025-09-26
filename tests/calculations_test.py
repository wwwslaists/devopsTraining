# System Modules
import sys
import os

# Installed Modules
import pytest

# Project Modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from calculations import area_of_circle, get_nth_fibonacci   # noqa: E402


def test_area_of_circle_positive_radius():
    """Test with a positive radius."""
    # Arrange
    radius = 1

    # Act
    result = area_of_circle(radius)

    def test_area_of_circle_negative_radius():
        """Test that a negative radius raises a ValueError."""
        with pytest.raises(ValueError) as excinfo:
            area_of_circle(-2)
        assert "Radius cannot be negative" in str(excinfo.value)


    def test_get_nth_fibonacci_negative():
        """Test that a negative n raises a ValueError."""
        with pytest.raises(ValueError) as excinfo:
            get_nth_fibonacci(-5)
        assert "n cannot be negative" in str(excinfo.value)


    def test_get_nth_fibonacci_two():
        """Test with n=2."""
        # Arrange & Act
        result = get_nth_fibonacci(2)
        
        # Assert
        assert result == 1


    def test_get_nth_fibonacci_three():
        """Test with n=3."""
        # Arrange & Act
        result = get_nth_fibonacci(3)
        
        # Assert
        assert result == 2
