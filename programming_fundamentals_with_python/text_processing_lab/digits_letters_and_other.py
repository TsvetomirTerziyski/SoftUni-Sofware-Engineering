def digits(text):
    digits = ''
    for char in text:
        if char.isdigit():
            digits += char
    return digits


def letters(text):
    letters = ''
    for char in text:
        if char.isalpha():
            letters += char
    return letters


def other(text):
    other = ''
    for char in text:
        if not char.isdigit() and not char.isalpha():
            other += char
    return other

text = input()
print(digits(text))
print(letters(text))
print(other(text))
