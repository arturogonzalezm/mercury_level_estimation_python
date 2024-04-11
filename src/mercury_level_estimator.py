from src.estimation_strategy import EstimationStrategy


class MercuryLevelEstimator:
    def __init__(self, strategy: EstimationStrategy):
        self._strategy = strategy

    def estimate_missing(self, readings):
        mercury_levels = []
        missing_indices = []
        for reading in readings:
            timestamp, value = reading.split('\t')
            if 'Missing' in value:
                missing_indices.append(len(mercury_levels))
                mercury_levels.append(None)
            else:
                mercury_levels.append(float(value))

        self._strategy.estimate(mercury_levels, missing_indices)

        for i in missing_indices:
            print(f"{mercury_levels[i]:.2f}")
