import numpy as np
from utils.input_getter import get_array

def calculate_grades_average(first_grades: np.array, second_grades: np.array) -> float:
    average_grades = np.array([0 for i in range(len(first_grades))])
    for i in range(len(first_grades)):
        average_grades[i] = (first_grades[i] + second_grades[i]) / 2


    highest_average = 0
    for grade in average_grades:
        if grade > highest_average:
            highest_average = grade

    return highest_average



print("enter the first grades")
first_array = get_array(6)

print("enter the second grades")
second_array = get_array(6)


print(calculate_grades_average(first_array, second_array))
