def shoot(sequence_list, indice, shot_power):
    if indice in range(len(sequence_list)):
        sequence_list[indice] -= shot_power
        if sequence_list[indice] <= 0:
            sequence_list.pop(indice)
    return sequence_list


def add(sequence_list, indice, value_to_add):
    if indice in range(len(sequence_list)):
        sequence_list.insert(indice, value_to_add)
    else:
        print("Invalid placement!")
    return sequence_list


def strike(sequence_list, strike_index, radius_of_strike):
    if strike_index in range(len(sequence_list)):
        start = strike_index - radius_of_strike
        end = strike_index + radius_of_strike

        if start in range(len(sequence_list)) and end in range(len(sequence_list)):
            del sequence_list[start:end+1]
        else:
            print('Strike missed!')
    else:
        print("Strike missed!")
    return sequence_list


sequence_of_targets = input().split()
integer_sequence = [int(i) for i in sequence_of_targets]

command = input().split()

while command[0] != 'End':
    if command[0] == 'Shoot':
        index, power = int(command[1]), int(command[2])
        integer_sequence = shoot(integer_sequence, index, power)
    elif command[0] == 'Add':
        index, value = int(command[1]), int(command[2])
        integer_sequence = add(integer_sequence, index, value)
    elif command[0] == 'Strike':
        index, radius = int(command[1]), int(command[2])
        integer_sequence = strike(integer_sequence, index, radius)

    command = input().split()

string_sequence = [str(i) for i in integer_sequence]
print('|'.join(string_sequence))
