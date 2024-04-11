from abc import ABC, abstractmethod


class EstimationStrategy(ABC):
    @abstractmethod
    def estimate(self, mercury_levels, missing_indices):
        pass
