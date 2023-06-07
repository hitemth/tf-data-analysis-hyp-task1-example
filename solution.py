import pandas as pd
import numpy as np

import math
from scipy.stats import norm

chat_id = 156287560 # Ваш chat ID, не меняйте название переменной

def solution(x_success: int, 
             x_cnt: int, 
             y_success: int, 
             y_cnt: int) -> bool:
    control_conversion = x_success / x_cnt
    test_conversion = y_success / y_cnt
    se = math.sqrt(control_conversion * (1 - control_conversion) / x_cnt + test_conversion * (1 - test_conversion) / y_cnt)
    z = (test_conversion - control_conversion) / se
    p_value = norm.sf(abs(z))
    return p_value <0.05 
