"""Module docstring: Test suite for the linear interpolation strategy.

This module contains tests for verifying the correctness and robustness of the
LinearInterpolationStrategy class.
"""
import os
import sys
import pytest

from src.linear_interpolation_strategy import LinearInterpolationStrategy

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))


def test_linear_interpolation_basic():
    """
    Test linear interpolation on a simple case with two missing values.
    """
    strategy = LinearInterpolationStrategy()
    mercury_levels = [100, None, 150, None, 200]
    missing_indices = [1, 3]
    strategy.estimate(mercury_levels, missing_indices)
    assert mercury_levels == [100, 125, 150, 175, 200], "Linear interpolation failed for basic input."


def test_linear_interpolation_with_invalid_types():
    """
    Test that the strategy raises a ValueError for non-float and non-None mercury_levels.
    """
    strategy = LinearInterpolationStrategy()
    mercury_levels = [100, "Invalid", 150]
    missing_indices = [1]
    with pytest.raises(ValueError, match="Mercury levels must be a list of floats or None."):
        strategy.estimate(mercury_levels, missing_indices)


def test_linear_interpolation_with_invalid_indices():
    """
    Test that the strategy raises a ValueError for invalid indices in the missing_indices list.
    :return: None
    """
    strategy = LinearInterpolationStrategy()
    mercury_levels = [100, None, 150]
    missing_indices = [1, 3]  # Index 3 is out of range.
    with pytest.raises(ValueError, match="Mercury levels must be a list of floats or None."):
        strategy.estimate(mercury_levels, missing_indices)
