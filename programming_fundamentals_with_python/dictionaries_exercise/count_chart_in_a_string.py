char_list = [char for char in input() if char != ' ']
occurrences = {}

for char in char_list:
    if char not in occurrences:
        occurrences[char] = 0
    occurrences[char] += 1

for character, occurrences in occurrences.items():
    print(f'{character} -> {occurrences}')
