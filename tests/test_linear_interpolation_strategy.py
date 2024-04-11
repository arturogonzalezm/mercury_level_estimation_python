"""Module docstring: Test suite for the linear interpolation strategy.

This module contains tests for verifying the correctness and robustness of the
LinearInterpolationStrategy class.
"""
import os
import sys
import pytest

from src.linear_interpolation_strategy import LinearInterpolationStrategy

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))


def test_estimate_success():
    """
    Test successful linear interpolation on a list with missing values.
    """
    strategy = LinearInterpolationStrategy()
    mercury_levels = [100, None, 150, None, 200]
    missing_indices = [1, 3]
    strategy.estimate(mercury_levels, missing_indices)
    assert mercury_levels == [100, 125, 150, 175, 200], "Interpolation failed for missing values."


def test_estimate_with_invalid_mercury_levels():
    """
    Test estimation with invalid mercury_levels input types.
    """
    strategy = LinearInterpolationStrategy()
    mercury_levels = ["invalid", None, 150]
    missing_indices = [1]
    with pytest.raises(ValueError, match="Mercury levels must be a list of floats or None."):
        strategy.estimate(mercury_levels, missing_indices)


def test_estimate_with_invalid_missing_indices():
    """
    Test estimation with invalid missing_indices (indices out of range).
    """
    strategy = LinearInterpolationStrategy()
    mercury_levels = [100, None, 150]
    missing_indices = [1, 5]  # 5 is out of range for mercury_levels list.
    with pytest.raises(ValueError,
                       match="Missing indices must be a list of valid integer indices of the mercury_levels list."):
        strategy.estimate(mercury_levels, missing_indices)
