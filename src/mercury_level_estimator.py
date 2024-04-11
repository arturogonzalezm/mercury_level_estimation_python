"""Module docstring: Implements the MercuryLevelEstimator class.

This module provides the MercuryLevelEstimator class, which utilizes a given
estimation strategy to estimate missing mercury levels in a set of readings.
"""

from src.estimation_strategy import EstimationStrategy


class MercuryLevelEstimator:
    """
    A class for estimating missing mercury levels in environmental readings.

    This class encapsulates the logic for applying a specific estimation strategy
    to a series of readings that contain missing mercury level data, enabling the
    estimation of those missing values.

    Attributes:
        _strategy (EstimationStrategy): The strategy to use for estimating missing mercury levels.
        _mercury_levels (List[float | None]): Internal storage of mercury levels, including estimated values.
    """

    def __init__(self, strategy: EstimationStrategy):
        """
        Initializes the MercuryLevelEstimator with a specific estimation strategy.

        Parameters:
            strategy (EstimationStrategy): The strategy to use for estimation.
        """
        self._strategy = strategy
        self._mercury_levels = []  # Initialize empty list for mercury levels

    def estimate_missing(self, readings):
        """
        Estimates missing mercury levels in the provided readings using the configured strategy.

        Processes the input readings to extract mercury levels and identify missing data points.
        Applies the configured estimation strategy to estimate the missing values.

        Parameters:
            readings (List[str]): A list of readings, each formatted as 'timestamp\tvalue'.
            Missing values are indicated by 'Missing_x'.

        Returns:
            None: The function updates internal state but does not return a value.
        """
        self._mercury_levels = []  # Reset mercury levels for each estimation run
        missing_indices = []

        for reading in readings:
            _, value = reading.split('\t')
            if 'Missing' in value:
                missing_indices.append(len(self._mercury_levels))
                self._mercury_levels.append(None)
            else:
                self._mercury_levels.append(float(value))

        # Apply the estimation strategy
        self._strategy.estimate(self._mercury_levels, missing_indices)

    def get_estimated_levels(self):
        """
        Retrieves the latest mercury levels, including any estimated values.

        Returns:
            List[float | None]: The mercury levels after estimation, with None representing
            any values that could not be estimated.
        """
        return self._mercury_levels
