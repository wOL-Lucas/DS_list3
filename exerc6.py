import numpy as np
from utils.input_getter import get_matrix, sum_array, array_length

def get_row_with_highest_average(grades: np.ndarray) -> int:
    highest_average = 0.0
    i = 0
    index = 0
    for row in grades:
        total = sum_array(row)
        length = array_length(row)

        average = total / length
        if average > highest_average:
            highest_average = average
            index = i

        i += 1    

    return index


grades = get_matrix(3, 3)

print(f"The highest average is from student number {get_row_with_highest_average(grades) + 1}")
