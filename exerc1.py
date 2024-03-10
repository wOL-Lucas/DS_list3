import numpy as np
from utils.input_getter import get_array

def replace_negative_numbers_for_zero(numbers:np.array) -> np.array:
    return np.array([0 if number < 0 else number for number in numbers])



array = get_array(5)
print(replace_negative_numbers_for_zero(array))
