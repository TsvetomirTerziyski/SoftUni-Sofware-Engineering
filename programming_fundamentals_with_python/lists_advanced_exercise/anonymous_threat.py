input_list = input().split()

while True:
    command = input()

    if command == '3:1':
        break

    command = command.split()

    if command[0] == 'merge':
        start_index = int(command[1])
        end_index = int(command[2])

        if start_index in range(len(input_list)) and end_index + 1 in range(len(input_list)):
            merged = ''.join(input_list[start_index: end_index + 1])
            input_list[start_index: end_index + 1] = [merged]
        elif start_index not in range(len(input_list)) and end_index + 1 in range(len(input_list)):
            start_index = 0
            merged = ''.join(input_list[start_index: end_index + 1])
            input_list[start_index: end_index + 1] = [merged]
        elif start_index in range(len(input_list)) and end_index + 1 not in range(len(input_list)):
            merged = ''.join(input_list[start_index:])
            input_list[start_index:] = [merged]
        elif start_index not in range(len(input_list)) and end_index + 1 not in range(len(input_list)):
            merged = ''.join(input_list[:])
            input_list[:] = [merged]

    if command[0] == 'divide':
        index = int(command[1])
        partitions = int(command[2])
        word = input_list.pop(index)
        divided_word = []

        if partitions > 0:
            step = len(word) // partitions

            for _ in range(partitions - 1):
                divided_word.append(word[0:step])
                word = word[step::]
            divided_word.append(word)
        else:
            divided_word.append(word)

        for idx in range(len(divided_word)):
            input_list.insert(idx + index, divided_word[idx])

print(' '.join(input_list))
