judges = int(input())

total_grades = 0
total_grades_sum = 0
grade_counter = 0

while True:
    presentation = input()

    if presentation == 'Finish':
        break

    grades_sum = 0

    for i in range(judges):
        grades_sum += float(input())

        grade_counter += 1
    total_grades_sum += grades_sum

    print(f"{presentation} - {grades_sum / judges:.2f}.")

print(f"Student's final assessment is {total_grades_sum/grade_counter:.2f}.")



