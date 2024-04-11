"""Module docstring: Defines the abstract base class for estimation strategies.

This module contains the abstract base class EstimationStrategy, which outlines
the necessary interface for all concrete estimation strategy implementations used
in estimating missing mercury levels.
"""

from abc import ABC, abstractmethod


class EstimationStrategy(ABC):
    """Abstract base class for mercury level estimation strategies.

    Defines the interface that all concrete estimation strategies must implement
    to be used for estimating missing mercury levels in the mercury level estimator.
    """

    @abstractmethod
    def estimate(self, mercury_levels, missing_indices):
        """
        Estimates the missing mercury levels based on provided indices.

        Parameters:
        - mercury_levels: List[float | None], the list of known and missing mercury levels,
          where missing levels are denoted by None.
        - missing_indices: List[int], indices in the mercury_levels list where the mercury
          levels are missing and need to be estimated.

        This method should modify the mercury_levels list in-place, filling in the missing
        values as per the specific strategy's logic.
        """
        pass
