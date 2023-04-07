from cmath import sqrt

import numpy as np

chat_id = 632165934  # Ваш chat ID, не меняйте название переменной
SIGMA = 0.011


def solution(p: float, x: np.array) -> tuple:
    alpha = 1 - p
    return np.mean(x) + alpha * sqrt(SIGMA) / sqrt(len(x)), \
        np.mean(x) + p * sqrt(SIGMA) / sqrt(len(x))
