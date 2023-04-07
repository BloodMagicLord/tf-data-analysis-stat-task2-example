import numpy as np
from scipy.stats import norm

chat_id = 632165934  # Ваш chat ID, не меняйте название переменной
SIGMA = 0.011


def solution(p: float, x: np.array) -> tuple:
    x -= SIGMA
    return (2 * x.mean() + 2 * np.sqrt(np.var(x)) * norm.ppf(p / 2) / np.sqrt(len(x))) + SIGMA, \
           (2 * x.mean() + 2 * np.sqrt(np.var(x)) * norm.ppf(1 - p / 2) / np.sqrt(len(x))) + SIGMA
