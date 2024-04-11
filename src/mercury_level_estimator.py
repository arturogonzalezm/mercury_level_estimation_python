"""Module docstring: Implements the MercuryLevelEstimator class.

This module provides the MercuryLevelEstimator class, which utilizes a given
estimation strategy to estimate missing mercury levels in a set of readings.
"""

from src.estimation_strategy import EstimationStrategy  # Adjust the import path as necessary


class MercuryLevelEstimator:
    """
    A class for estimating missing mercury levels in environmental readings.

    Attributes:
        _strategy (EstimationStrategy): The strategy to use for estimating missing mercury levels.
    """

    def __init__(self, strategy: EstimationStrategy):
        """
        Initializes the MercuryLevelEstimator with a specific estimation strategy.

        Parameters:
            strategy (EstimationStrategy): The strategy to use for estimation.
        """
        self._strategy = strategy

    def estimate_missing(self, readings):
        """
        Estimates missing mercury levels in the provided readings using the configured strategy.

        Parameters:
            readings (List[str]): A list of readings, where each reading is a string formatted
            as 'timestamp\tvalue'. Missing values are indicated by 'Missing_x'.
        """
        mercury_levels = []
        missing_indices = []
        for reading in readings:
            _, value = reading.split('\t')  # Adjusted to use underscore for unused variable
            if 'Missing' in value:
                missing_indices.append(len(mercury_levels))
                mercury_levels.append(None)
            else:
                mercury_levels.append(float(value))

        self._strategy.estimate(mercury_levels, missing_indices)

        for i in missing_indices:
            print(f"{mercury_levels[i]:.2f}")
