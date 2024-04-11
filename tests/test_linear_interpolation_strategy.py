import pytest

from src.linear_interpolation_strategy import LinearInterpolationStrategy


def test_linear_interpolation_basic():
    strategy = LinearInterpolationStrategy()
    mercury_levels = [100, None, 150, None, 200]
    missing_indices = [1, 3]
    strategy.estimate(mercury_levels, missing_indices)
    assert mercury_levels == [100, 125, 150, 175, 200], "Failed to linearly interpolate correctly"


def test_linear_interpolation_no_missing():
    strategy = LinearInterpolationStrategy()
    mercury_levels = [100, 120, 140]
    missing_indices = []
    strategy.estimate(mercury_levels, missing_indices)
    assert mercury_levels == [100, 120, 140], "Altered data with no missing values"
