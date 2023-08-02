student_name = input()

years_counter = 0
sum_grades = 0
negative_grade_counter = 0
average_grade = 0

while True:
    grade = float(input())

    if grade < 4:
        negative_grade_counter += 1
        if negative_grade_counter == 2:
            print(f'{student_name} has been excluded at {years_counter+1} grade')
            break

    else:
        years_counter += 1
        sum_grades += grade

    if years_counter == 12:
        average_grade = sum_grades / 12
        print(f'{student_name} graduated. Average grade: {average_grade:.2f}')
        break












