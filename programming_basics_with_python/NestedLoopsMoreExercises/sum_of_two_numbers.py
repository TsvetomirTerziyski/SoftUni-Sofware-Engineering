interval_beginning = int(input())
interval_ending = int(input())
magic_number = int(input())

counter = 0
flag = False

for n1 in range(interval_beginning, interval_ending + 1):
    for n2 in range(interval_beginning, interval_ending + 1):

        counter += 1

        if n1 + n2 == magic_number:
            flag = True
            print(f'Combination N:{counter} ({n1} + {n2} = {magic_number})')

    if flag:
        break
else:
    print(f'{counter} combinations - neither equals {magic_number}')


