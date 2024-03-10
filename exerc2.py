import numpy as np
from utils.input_getter import get_array


def sum_positive_and_count_negative(numbers: np.array) -> tuple[int, int]:
    zero_count = 0
    positive_sum = 0
    for number in numbers:
        if number < 0:
            zero_count += 1
        else:
            positive_sum += number

    return positive_sum, zero_count

array = get_array(5)

print(sum_positive_and_count_negative(array))
