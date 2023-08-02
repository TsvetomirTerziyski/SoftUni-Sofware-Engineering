free_space = int(input()) * int(input()) * int(input())

total_space = 0

while True:
    space = input()

    if space == 'Done':
        if total_space < free_space:
            print(f'{free_space - total_space} Cubic meters left.')
            break

    total_space += int(space)

    if total_space > free_space:
        print(f'No more free space! You need {total_space - free_space} Cubic meters more.')
        break

