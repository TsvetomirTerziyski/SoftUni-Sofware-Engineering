negative_marks = int(input())
negative_counter = 0
task_counter = 0
average_score = 0
last_task = ""
sum_marks = 0

while True:
    task_name = input()

    if task_name == 'Enough':
        print(f'Average score: {average_score:.2f}')
        print(f'Number of problems: {task_counter}')
        print(f'Last problem: {last_task}')
        break

    mark = int(input())

    task_counter += 1
    last_task = task_name
    sum_marks += mark
    average_score = sum_marks / task_counter

    if mark <= 4:
        negative_counter += 1
        if negative_counter == negative_marks:
            print(f'You need a break, {negative_counter} poor grades.')
            break