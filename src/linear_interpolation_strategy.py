from src.estimation_strategy import EstimationStrategy


class LinearInterpolationStrategy(EstimationStrategy):
    def estimate(self, mercury_levels, missing_indices):
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
                mercury_levels[i] = 0  # Fallback
