def contains_substring(activation_key, substring_to_check):
    if substring_to_check in activation_key:
        return f"{activation_key} contains {substring}"
    return "Substring not found!"


def flip_substring(activation_key, lower_or_upper, start_index, end_index):
    first_part = activation_key[:start_index]
    second_part = activation_key[end_index:]
    substring = activation_key[start_index:end_index]

    if lower_or_upper == 'Lower':
        activation_key = first_part + substring.lower() + second_part
    else:
        activation_key = first_part + substring.upper() + second_part

    return activation_key


def substring_slicing(activation_key, start_index, end_index):
    first_part = activation_key[:start_index]
    second_part = activation_key[end_index:]
    activation_key = first_part + second_part
    return activation_key


raw_activation_key = input()
command = input().split('>>>')

while command[0] != "Generate":
    if command[0] == 'Contains':
        substring = command[1]
        print(contains_substring(raw_activation_key, substring))
    elif command[0] == 'Flip':
        upper_or_lower, start_index, end_index = command[1], int(command[2]), int(command[3])
        raw_activation_key = flip_substring(raw_activation_key, upper_or_lower, start_index, end_index)
        print(raw_activation_key)
    elif command[0] == 'Slice':
        start_index, end_index = int(command[1]), int(command[2])
        raw_activation_key = substring_slicing(raw_activation_key, start_index, end_index)
        print(raw_activation_key)

    command = input().split('>>>')

print(f"Your activation key is: {raw_activation_key}")
