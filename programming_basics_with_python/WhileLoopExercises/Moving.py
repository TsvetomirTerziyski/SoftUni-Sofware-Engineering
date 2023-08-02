total = int(input()) * int(input()) * int(input())
sum_space = 0

while True:
    space = input()

    if space == 'Done':
        print(f'{total - sum_space} Cubic meters left.')
        break

    space = int(space)
    sum_space += space

    if sum_space > total:
        print(f'No more free space! You need {sum_space - total} Cubic meters more.')
        break
