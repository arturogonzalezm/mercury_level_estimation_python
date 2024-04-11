"""Module docstring: Test suite for the linear interpolation strategy.

This module contains tests for verifying the correctness and robustness of the
LinearInterpolationStrategy class.
"""

from src.linear_interpolation_strategy import LinearInterpolationStrategy


def test_linear_interpolation_basic():
    """
    Test that verifies linear interpolation fills in missing mercury levels correctly.

    Ensures that given a list of mercury levels with some missing values, the
    LinearInterpolationStrategy correctly estimates those missing values based
    on linear interpolation between the nearest non-missing values.
    """
    strategy = LinearInterpolationStrategy()
    mercury_levels = [100, None, 150, None, 200]
    missing_indices = [1, 3]
    strategy.estimate(mercury_levels, missing_indices)
    assert mercury_levels == [100, 125, 150, 175, 200], "Failed to linearly interpolate correctly"


def test_linear_interpolation_no_missing():
    """
    Test that verifies behavior with no missing mercury levels.

    Ensures that if the input list of mercury levels does not contain any missing
    values, the LinearInterpolationStrategy leaves the list unchanged.
    """
    strategy = LinearInterpolationStrategy()
    mercury_levels = [100, 120, 140]
    missing_indices = []
    strategy.estimate(mercury_levels, missing_indices)
    assert mercury_levels == [100, 120, 140], "Altered data with no missing values"
