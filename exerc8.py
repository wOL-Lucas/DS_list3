import numpy as np 
from utils.input_getter import get_matrix

def sum_diagonal(matrix: np.ndarray) -> int:
    total = 0
    for i in range(len(matrix)):
        print(matrix[i][i])
        total += matrix[i][i]
    
    return total


matrix = get_matrix(3, 3)
print(sum_diagonal(matrix))
