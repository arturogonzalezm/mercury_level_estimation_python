import pytest

from src.linear_interpolation_strategy import LinearInterpolationStrategy
from src.mercury_level_estimator import MercuryLevelEstimator


def test_mercury_level_estimator_with_linear_interpolation():
    readings = ["2023-01-01\t100", "2023-01-02\tMissing_1", "2023-01-03\t150"]
    strategy = LinearInterpolationStrategy()
    estimator = MercuryLevelEstimator(strategy)
    estimated_levels = estimator.estimate_missing(readings)
    assert estimated_levels == [100, 125, 150], "Failed to estimate missing levels correctly"
