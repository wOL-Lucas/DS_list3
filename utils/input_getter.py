import numpy as np


def input_getter():
    return int(input("Enter a number: "))

def get_array(length: int) -> np.array:
    array = np.array([0 for i in range(length)])
    for i in range(length):
        array[i] = input_getter()
    return array



def get_matrix(rows: int, columns: int) -> np.ndarray:
    matrix = np.array([[0 for i in range(columns)] for j in range(rows)])
    for i in range(rows):
        print(f"Enter the {columns} elements of row {i + 1}")
        for j in range(columns):
            matrix[i][j] = input_getter()

    return matrix



