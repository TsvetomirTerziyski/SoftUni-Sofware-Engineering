text = input()

new_text = [letter for letter in text if letter.lower() not in ['a', 'o', 'u', 'e', 'i']]
print(''.join(new_text))
