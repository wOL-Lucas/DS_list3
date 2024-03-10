import numpy as np


def replace_negative_numbers_for_zero(numbers:np.array) -> np.array:
    return np.array([0 if number < 0 else number for number in numbers])



array = np.array([1, -2, -3, 4, 5])

print(replace_negative_numbers_for_zero(array))
