final_string = ''
while True:

    command = input()

    if command == 'End':
        break

    string = command

    if string == 'SoftUni':
        continue

    for symbol in string:
        final_string += symbol * 2
    print(final_string)
    final_string = ''
