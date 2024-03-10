import numpy as np



def sum_positive_and_count_negative(numbers: np.array) -> tuple[int, int]:
    zero_count = 0
    positive_sum = 0
    for number in numbers:
        if number < 0:
            zero_count += 1
        else:
            positive_sum += number

    return positive_sum, zero_count



array = np.array([1, -2, -3, 4, 5])
print(sum_positive_and_count_negative(array))
