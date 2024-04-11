from src.mercury_level_estimator import MercuryLevelEstimator
from src.linear_interpolation_strategy import LinearInterpolationStrategy

if __name__ == "__main__":
    readings = []
    with open('data/input000.txt', 'r') as file:
        readings_count = int(file.readline().strip())
        for _ in range(readings_count):
            readings_item = file.readline().strip()
            readings.append(readings_item)

    estimator = MercuryLevelEstimator(LinearInterpolationStrategy())
    estimator.estimate_missing(readings)
