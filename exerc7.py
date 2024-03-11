import numpy as np
from utils.input_getter import get_matrix

def find_first_duplicate(matrix: np.ndarray) -> tuple[int, int, int]:
    row_index = 0
    column_index = 0

    _row_index = 0
    _column_index = 0

    for row in matrix:
        for element in row:
            for _row in matrix:
                for _element in _row:
                    if element == _element and row_index != _row_index:
                        return (_row_index, _column_index, _element)
                    
                    _column_index += 1

                _column_index = 0
                _row_index += 1
            
            _column_index = 0
            _row_index = 0

            column_index += 1
        row_index += 1
    return (-1, -1, -1)


matrix = get_matrix(5, 5)

row_index, column_index, element = find_first_duplicate(matrix)
print(f"The first duplicate is at row {row_index + 1} ({row_index}), column {column_index + 1} ({column_index}) and it's value is {element}")
