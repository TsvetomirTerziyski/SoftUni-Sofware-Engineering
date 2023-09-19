input_list = [int(i) for i in input().split()]

while True:
    command = input()

    if command == 'end':
        break

    command = command.split()

    if command[0] == 'swap':
        first_index, second_index = int(command[1]), int(command[2])
        input_list[first_index], input_list[second_index] = input_list[second_index], input_list[first_index]
    elif command[0] == 'multiply':
        first_index, second_index = int(command[1]), int(command[2])
        input_list[first_index] = input_list[first_index] * input_list[second_index]
    elif command[0] == 'decrease':
        for index in range(len(input_list)):
            input_list[index] -= 1

print(', '.join([str(i) for i in input_list]))
