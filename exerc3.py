import numpy as np
from utils.input_getter import input_getter

# both arrays will be 6 elements long
def calculate_grades_average(first_grades: np.array, second_grades: np.array) -> float:
    average_grades = np.array([0 for i in range(len(first_grades))])
    for i in range(len(first_grades)):
        average_grades[i] = (first_grades[i] + second_grades[i]) / 2


    highest_average = 0
    for grade in average_grades:
        if grade > highest_average:
            highest_average = grade

    return highest_average


max_of_numbers = 6
first_array = np.array([0 for i in range(max_of_numbers)])
second_array = np.array([0 for i in range(max_of_numbers)])

print("enter the first grades")
for i in range(max_of_numbers):
    first_array[i] = input_getter()

print("enter the second grades")
for i in range(max_of_numbers):
    second_array[i] = input_getter()

print(calculate_grades_average(first_array, second_array))
