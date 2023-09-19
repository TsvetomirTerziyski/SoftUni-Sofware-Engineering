def add_stop(input_string, index_for_string, string_to_add):
    if index_for_string in range(len(input_string)):
        first_part = input_string[:index_for_string]
        second_part = string_to_add
        last_part = input_string[index_for_string:]
        input_string = first_part + second_part + last_part
    return input_string


def remove_stop(input_string, first_index, last_index):
    if first_index in range(len(input_string)) and last_index in range(len(input_string)):
        first_part = input_string[:first_index]
        last_part = input_string[last_index + 1:]
        input_string = first_part + last_part
    return input_string


def switch(input_string, string_to_switch, string_to_add):
    if string_to_switch in input_string:
        input_string = input_string.replace(string_to_switch, string_to_add)
    return input_string


string_input = input()
command = input().split(':')

while command[0] != 'Travel':
    if command[0] == 'Add Stop':
        index, string = int(command[1]), command[2]
        string_input = add_stop(string_input, index, string)
        print(string_input)
    elif command[0] == 'Remove Stop':
        start_index, end_index = int(command[1]), int(command[2])
        string_input = remove_stop(string_input, start_index, end_index)
        print(string_input)
    elif command[0] == 'Switch':
        old_string, new_string = command[1], command[2]
        string_input = switch(string_input, old_string, new_string)
        print(string_input)
    command = input().split(':')

print(f"Ready for world tour! Planned stops: {string_input}")
