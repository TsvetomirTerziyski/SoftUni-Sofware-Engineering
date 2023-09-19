def take_odd(string):
    return string[1::2]


def cut(string, start_index, slice_length):
    first_part = string[:start_index]
    cut_part = string[start_index:start_index + slice_length]
    last_part = string[start_index + slice_length:]
    string = first_part + last_part
    return string


def substitute_of_string(string, substring_to_take, substitute_string):
    if substring_to_take in string:
        return string.replace(substring_to_take, substitute_string)
    else:
        return f"Nothing to replace!"


input_string = input()

command = input().split()

while command[0] != 'Done':
    if command[0] == 'TakeOdd':
        input_string = take_odd(input_string)
        print(input_string)
    elif command[0] == 'Cut':
        index, length = int(command[1]), int(command[2])
        input_string = cut(input_string, index, length)
        print(input_string)
    elif command[0] == 'Substitute':
        substring, substitute = command[1], command[2]
        if substring in input_string:
            input_string = substitute_of_string(input_string, substring, substitute)
            print(input_string)
        else:
            print(substitute_of_string(input_string, substring, substitute))

    command = input().split()

print(f"Your password is: {input_string}")
