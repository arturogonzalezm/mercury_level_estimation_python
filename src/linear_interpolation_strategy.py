import logging

from src.estimation_strategy import EstimationStrategy  # Adjust the import path as necessary

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


class LinearInterpolationStrategy(EstimationStrategy):
    """
    Implements estimation of missing mercury levels using linear interpolation.
    """

    def validate_mercury_levels(self, mercury_levels):
        """
        Validates that all items in mercury_levels are either floats or None.
        Raises a ValueError if the validation fails.
        """
        if not all(isinstance(x, (float, type(None))) for x in mercury_levels):
            logger.error("Mercury levels list contains non-float and non-None types.")
            raise ValueError("Mercury levels must be a list of floats or None.")

    def validate_missing_indices(self, mercury_levels, missing_indices):
        """
        Validates that all items in missing_indices are valid integer indices
        within the bounds of the mercury_levels list.
        Raises a ValueError if the validation fails.
        """
        if not all(isinstance(x, int) for x in missing_indices) or any(
                x >= len(mercury_levels) for x in missing_indices):
            logger.error("Invalid indices in the missing_indices list.")
            raise ValueError("Missing indices must be a list of valid integer indices of the mercury_levels list.")

    def estimate(self, mercury_levels, missing_indices):
        """
        Estimates missing mercury levels using linear interpolation.

        First, it validates the input arguments using the dedicated validation methods.
        Then, it proceeds with the interpolation logic if the validation passes.
        """
        # Perform validation checks
        self.validate_missing_indices(mercury_levels, missing_indices)
        self.validate_mercury_levels(mercury_levels)

        # Estimation logic
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

                # Interpolation calculation
                if before is not None and after is not None:
                    mercury_levels[i] = (before + after) / 2
                elif before is not None:
                    mercury_levels[i] = before
                elif after is not None:
                    mercury_levels[i] = after
                else:
                    mercury_levels[i] = 0  # Default to 0 if no surrounding non-missing values
                    logger.warning(f"No surrounding non-missing values for index {i}; defaulted to 0.")

            for i in missing_indices:
                logging.info(f"{mercury_levels[i]:.2f}")

            logger.info("Missing mercury levels estimated successfully.")
        except Exception as e:
            logger.error(f"An error occurred during estimation: {str(e)}")
            raise
