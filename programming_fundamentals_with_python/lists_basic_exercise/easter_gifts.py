gifts = input().split()

while True:
    command = input().split()

    if command[0] == 'No' and command[1] == 'Money':
        break

    index = 0

    if command[0] == 'OutOfStock':
        for index, element in enumerate(gifts):
            if command[1] == element:
                gifts[index] = 'None'
    elif command[0] == 'Required':
        index = int(command[2])
        if 0 <= index < len(gifts):
            gifts[index] = command[1]
    elif command[0] == 'JustInCase':
        gifts[-1] = command[1]

while 'None' in gifts:
    gifts.remove('None')

print((' ').join(gifts))
