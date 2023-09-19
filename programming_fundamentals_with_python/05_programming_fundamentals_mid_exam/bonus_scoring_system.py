from math import ceil

number_of_students = int(input())
number_of_lectures = int(input())
additional_bonus = int(input())

max_bonus = 0
attendances_of_student_with_max_bonus = 0

for _ in range(number_of_students):

    count_of_attendances = int(input())

    total_bonus = count_of_attendances / number_of_lectures * (5 + additional_bonus)
    if total_bonus > max_bonus:
        max_bonus = total_bonus
        attendances_of_student_with_max_bonus = count_of_attendances

print(f"Max Bonus: {ceil(max_bonus)}.")
print(f"The student has attended {attendances_of_student_with_max_bonus} lectures.")
