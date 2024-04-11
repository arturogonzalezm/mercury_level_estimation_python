"""Module docstring: Test suite for MercuryLevelEstimator.

This module contains pytest tests for the MercuryLevelEstimator class,
particularly focusing on its ability to correctly estimate missing mercury
levels using different strategies, starting with the LinearInterpolationStrategy.
"""

from src.linear_interpolation_strategy import LinearInterpolationStrategy
from src.mercury_level_estimator import MercuryLevelEstimator


def test_mercury_level_estimator_with_linear_interpolation():
    """
    Test MercuryLevelEstimator's handling of missing levels with linear interpolation.

    Validates that MercuryLevelEstimator, when configured with the
    LinearInterpolationStrategy, accurately interpolates and fills in missing
    mercury levels within a provided set of readings.
    """
    readings = ["2023-01-01\t100", "2023-01-02\tMissing_1", "2023-01-03\t150"]
    strategy = LinearInterpolationStrategy()
    estimator = MercuryLevelEstimator(strategy)

    estimator.estimate_missing(readings)

    # Assuming a method like get_estimated_levels() exists to retrieve the internal state after estimation
    estimated_levels = estimator.get_estimated_levels()

    assert estimated_levels == [100, 125, 150], "Failed to estimate missing levels correctly"

