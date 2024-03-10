import numpy as np
from utils.input_getter import get_array


def sort_array(array: np.array) -> np.array:
    for i in range(len(array)):
        for j in range(len(array) - 1):
            current_element = array[i]
            previous_element = array[j]
            if current_element < previous_element:
                array[i] = previous_element
                array[j] = current_element

    return array

array = get_array(5)

print(sort_array(array))
