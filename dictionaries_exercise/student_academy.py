row_pairs = int(input())
average_grades_dict = {}

for i in range(row_pairs):
    name = input()
    grade = float(input())
    if name not in average_grades_dict:
        average_grades_dict[name] = grade
    else:
        average_grades_dict[name] += grade
        average_grades_dict[name] /= 2


new_dict = {name: grade for name, grade in average_grades_dict.items() if average_grades_dict[name] >= 4.50}

for name, average_grades in new_dict.items():
    print(f"{name} -> {average_grades:.2f}")
