import numpy as np


def input_getter():
    return int(input("Enter a number: "))

def get_array(length: int) -> np.array:
    array = np.array([0 for i in range(length)])
    for i in range(length):
        array[i] = input_getter()
    return array
