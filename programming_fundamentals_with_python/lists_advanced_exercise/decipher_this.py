input_list = input().split(' ')

for element in input_list:
    ascii_elements = [number for number in element if number.isnumeric()]
    letters = [letter for letter in element if letter not in ascii_elements]

    ascii_joined = ''.join(ascii_elements)
    ascii_to_char = chr(int(ascii_joined))

    swapped_letters = letters[0], letters[-1] = letters[-1], letters[0]
    joined_letters = ''.join(letters)

    print(ascii_to_char + joined_letters, end=' ')
