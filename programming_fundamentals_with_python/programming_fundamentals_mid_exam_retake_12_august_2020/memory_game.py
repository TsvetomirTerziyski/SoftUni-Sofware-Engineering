input_list = input().split()
moves = 0

while True:
    command = input()

    if command == 'end' and len(input_list) > 0:
        print(f"Sorry you lose :(\n{' '.join(input_list)}")
        break
    elif command == 'end':
        break

    first_index, second_index = [int(i) for i in command.split()]

    if first_index == second_index or \
        (first_index not in range(len(input_list))) or \
        (second_index not in range(len(input_list))):

        moves += 1
        for _ in range(2):
            input_list.insert(len(input_list)//2, f"-{moves}a")

        print("Invalid input! Adding additional elements to the board")
        continue

    if input_list[first_index] == input_list[second_index]:
        if first_index > second_index:
            matching_first = input_list.pop(first_index)
            matching_second = input_list.pop(second_index)
        else:
            matching_first = input_list.pop(first_index)
            matching_second = input_list.pop(second_index-1)
        moves += 1
        print(f"Congrats! You have found matching elements - {matching_first}!")

    elif input_list[first_index] != input_list[second_index]:
        moves += 1
        print("Try again!")

    if len(input_list) == 0:
        print(f"You have won in {moves} turns!")
        break
