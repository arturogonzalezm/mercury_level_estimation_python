"""Module docstring: Implements LinearInterpolationStrategy for estimating missing values.

This module provides an implementation of the EstimationStrategy abstract base class,
using linear interpolation to estimate and fill in missing mercury levels in a series
of environmental readings.
"""

from src.estimation_strategy import EstimationStrategy  # Adjust the import path as necessary


class LinearInterpolationStrategy(EstimationStrategy):
    """
    Implements estimation of missing mercury levels using linear interpolation.

    Linear interpolation is used to estimate missing values based on the nearest
    known values before and after the missing entry.
    """

    def estimate(self, mercury_levels, missing_indices):
        """
        Fills in missing mercury levels using linear interpolation.

        Parameters:
        - mercury_levels: List of known and missing mercury levels, with missing
          values represented by None.
        - missing_indices: Indices of missing values in the mercury_levels list.

        Modifies the mercury_levels list in-place by replacing None values with
        estimated values based on linear interpolation.
        """
        for i in missing_indices:
            before = after = None
            for j in range(i - 1, -1, -1):
                if mercury_levels[j] is not None:
                    before = mercury_levels[j]
                    break
            for k in range(i + 1, len(mercury_levels)):
                if mercury_levels[k] is not None:
                    after = mercury_levels[k]
                    break
            if before is not None and after is not None:
                mercury_levels[i] = (before + after) / 2
            elif before is not None:
                mercury_levels[i] = before
            elif after is not None:
                mercury_levels[i] = after
            else:
                mercury_levels[i] = 0  # Fallback for cases where no surrounding values are available
