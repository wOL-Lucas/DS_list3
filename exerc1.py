import numpy as np
from utils.input_getter import input_getter

def replace_negative_numbers_for_zero(numbers:np.array) -> np.array:
    return np.array([0 if number < 0 else number for number in numbers])



max_of_numbers = 5
array = np.array([0 for i in range(max_of_numbers)])
for i in range(max_of_numbers):
    array[i] = input_getter()


print(replace_negative_numbers_for_zero(array))
