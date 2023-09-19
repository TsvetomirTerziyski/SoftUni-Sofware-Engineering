def replaced_text(text):
    last_char = ''
    new_text = ''

    for char in text:
        if char != last_char:
            new_text += char
            last_char = char
    return new_text


text = input()
print(replaced_text(text))
