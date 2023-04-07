from cmath import sqrt

import numpy as np
from scipy.stats import norm

chat_id = 632165934  # Ваш chat ID, не меняйте название переменной
SIGMA = 0.011


def solution(p: float, x: np.array) -> tuple:
    alpha = 1 - p
    x -= SIGMA
    return x.mean() - np.sqrt(np.var(x)) * norm.ppf(alpha / 2) / np.sqrt(len(x)) + SIGMA, \
           x.mean() - np.sqrt(np.var(x)) * norm.ppf(p / 2) / np.sqrt(len(x)) + SIGMA