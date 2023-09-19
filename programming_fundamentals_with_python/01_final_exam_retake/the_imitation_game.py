def move_letters(message, num_letters):
    removed_part = message[:num_letters]
    left_part = message[num_letters:]
    message = left_part + removed_part
    return message


def insert_value(message, insert_index, insert_value):
    before_insertion = message[:insert_index]
    last_part = message[insert_index:]
    message = before_insertion + insert_value + last_part
    return message


def change_all(message, substring_to_change, replacement_substring):
    return message.replace(substring_to_change, replacement_substring)


encrypted_message = input()

string_operation = input().split('|')

while string_operation[0] != 'Decode':
    if string_operation[0] == 'Move':
        number_of_letters = int(string_operation[1])
        encrypted_message = move_letters(encrypted_message, number_of_letters)
    elif string_operation[0] == 'Insert':
        index, value = int(string_operation[1]), string_operation[2]
        encrypted_message = insert_value(encrypted_message, index, value)
    elif string_operation[0] == 'ChangeAll':
        substring, replacement = string_operation[1], string_operation[2]
        encrypted_message = change_all(encrypted_message, substring, replacement)

    string_operation = input().split('|')

print(f"The decrypted message is: {encrypted_message}")
