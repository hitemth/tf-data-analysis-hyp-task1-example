import pandas as pd
import numpy as np

import math
from scipy.stats import norm

chat_id = 156287560 # Ваш chat ID, не меняйте название переменной

def solution(x_success: int, 
             x_cnt: int, 
             y_success: int, 
             y_cnt: int) -> bool:
    from statsmodels.stats.proportion import proportions_ztest
    count = np.array([x_success, y_success])
    nobs = np.array([x_cnt, y_cnt])
    p_val = proportions_ztest(count, nobs, alternative='larger')[1]
    return p_val <= 0.05
