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

    # Assert
    assert abs(result - 3.14159) < 1e-5


def test_area_of_circle_zero_radius():
    """Test with a radius of zero."""
    # Arrange
    radius = 0

    # Act
    result = area_of_circle(radius)

    # Assert
    assert result == 0


def test_get_nth_fibonacci_zero():
    """Test with n=0."""
    # Arrange
    n = 0

    # Act
    result = get_nth_fibonacci(n)

    # Assert
    assert result == 0


def test_get_nth_fibonacci_one():
    """Test with n=1."""
    # Arrange
    n = 1

    # Act
    result = get_nth_fibonacci(n)

    # Assert
    assert result == 1

def test_get_nth_fibonacci_ten():
 """Test with n=10."""
 # Arrange
 n = 10

 # Act
 result = get_nth_fibonacci(n)

 # Assert
 assert result == 55

 # ...existing code...

def test_area_of_circle_with_float():
    """Test with a floating point radius."""
    # Arrange
    radius = 2.5
    expected = 3.14159 * radius**2

    # Act
    result = area_of_circle(radius)

    # Assert
    assert abs(result - expected) < 1e-5


def test_get_nth_fibonacci_five():
    """Test with n=5."""
    # Arrange
    n = 5
    expected = 5  # Fibonacci sequence: 0, 1, 1, 2, 3, 5,...

    # Act
    result = get_nth_fibonacci(n)

    # Assert
    assert result == expected
