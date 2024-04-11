"""Module docstring: Implements LinearInterpolationStrategy for estimating missing values.

This module provides an implementation of the EstimationStrategy abstract base class,
using linear interpolation to estimate and fill in missing mercury levels in a series
of environmental readings.
"""

import logging

from src.estimation_strategy import EstimationStrategy  # Adjust the import path as necessary

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


class LinearInterpolationStrategy(EstimationStrategy):
    """
    Implements estimation of missing mercury levels using linear interpolation.
    """

    def estimate(self, mercury_levels, missing_indices):
        """
        Fills in missing mercury levels using linear interpolation.
        """
        if not all(isinstance(x, (float, type(None))) for x in mercury_levels):
            logging.error("Mercury levels list contains non-float and non-None types.")
            raise ValueError("Mercury levels must be a list of floats or None.")

        if not all(isinstance(x, int) for x in missing_indices) or any(
                x >= len(mercury_levels) for x in missing_indices):
            logging.error("Invalid indices in the missing_indices list.")
            raise ValueError("Missing indices must be a list of valid integer indices of the mercury_levels list.")

        try:
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
                    mercury_levels[i] = 0  # Log a warning about missing surrounding values
                    logging.warning(f"No surrounding non-missing values for index {i}; defaulted to 0.")

            for i in missing_indices:
                logging.info(f"{mercury_levels[i]:.2f}")

            logging.info("Missing mercury levels estimated successfully.")
        except Exception as e:
            logging.error(f"An error occurred during estimation: {str(e)}")
            raise
