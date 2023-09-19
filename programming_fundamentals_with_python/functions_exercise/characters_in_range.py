def characters_between_two(char_one, char_two):
    for character in range(ord(char_one) + 1, ord(char_two)):
        char_list.append(chr(character))
    return char_list


first_character = input()
second_character = input()
char_list = []

print(" ".join(characters_between_two(first_character, second_character)))
