student_dict = {}

while True:
    command = input()

    if ':' not in command:
        for k, v in student_dict.items():
            if command[0:5] in v[1]:
                print(f'{k} - {v[0]}')
        break

    splitted = command.split(':')

    student_name, ID, course = splitted[0], splitted[1], splitted[2]

    student_dict[student_name] = [ID, course]
