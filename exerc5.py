import numpy as np
from utils.input_getter import get_matrix

def is_all_elements_even(matrix: np.ndarray) -> bool:
    for row in matrix:
        for element in row:
            if element % 2 != 0:
                return False

    return True


matrix = get_matrix(3, 3)

print(is_all_elements_even(matrix))
