"""Main script for estimating missing mercury levels in environmental readings.

This script reads a series of readings from 'data/input000.txt', where each reading
consists of a timestamp and either a mercury level or a placeholder for missing data.
It utilizes the LinearInterpolationStrategy through the MercuryLevelEstimator to estimate
and fill in the missing mercury levels.
"""

from src.mercury_level_estimator import MercuryLevelEstimator
from src.linear_interpolation_strategy import LinearInterpolationStrategy

if __name__ == "__main__":
    readings = []
    # Specify encoding to ensure consistent behavior across different environments
    with open('data/input000.txt', 'r', encoding='utf-8') as file:
        readings_count = int(file.readline().strip())
        for _ in range(readings_count):
            readings_item = file.readline().strip()
            readings.append(readings_item)

    estimator = MercuryLevelEstimator(LinearInterpolationStrategy())
    estimator.estimate_missing(readings)
