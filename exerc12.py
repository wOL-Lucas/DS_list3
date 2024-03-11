import numpy as np 

def get_only_commons(first_array: np.array, second_array: np.array) -> np.array:
    return np.array([element for element in first_array if element in second_array])



first_array = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
second_array = np.array([2, 4, 6, 8, 10, 12, 14, 16, 18])


print(get_only_commons(first_array, second_array))
