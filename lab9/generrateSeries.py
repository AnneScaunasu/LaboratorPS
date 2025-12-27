import numpy as np


def generate_series(N = 1000):
    t = np.arange(0, 1, 1 / N)
    trend = np.random.randint(100) * (t ** 2) + np.random.randint(100) * t - np.random.randint(100)
    first_cos, second_cos = np.random.randint(100), np.random.randint(100)
    # print(first_cos)
    # print(second_cos)
    season = np.cos(2 * np.pi * t * first_cos) + np.cos(2 * np.pi * t * second_cos)
    noise = np.random.normal(0, 1, N)
    return trend, season, noise

