sequence = [int(i) for i in input().split()]
shot_targets = 0

while True:
    command_to_use = input()

    if command_to_use == 'End':
        string_sequence = [str(element) for element in sequence]
        print(f"Shot targets: {shot_targets} -> {' '.join(string_sequence)}")
        break
    if int(command_to_use) in range(len(sequence)):
        current_number = sequence[int(command_to_use)]
        for i in range(len(sequence)):
            if sequence[i] != -1:
                if sequence[i] > current_number:
                    sequence[i] -= current_number
                else:
                    sequence[i] += current_number

        sequence[int(command_to_use)] = -1
        shot_targets += 1
