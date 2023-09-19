first_employee_capacity = int(input())
second_employee_capacity = int(input())
third_employee_capacity = int(input())
students_count = int(input())

hours = 0
students_per_hour = first_employee_capacity + second_employee_capacity + third_employee_capacity

while students_count > 0:
    hours += 1
    if hours % 4 == 0:
        continue

    students_count -= students_per_hour

print(f"Time needed: {hours}h.")
