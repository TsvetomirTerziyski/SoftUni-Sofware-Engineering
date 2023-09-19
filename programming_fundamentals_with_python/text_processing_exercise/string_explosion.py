def explosion(text):
    strength = 0
    text_after_explosion = ''

    for index in range(len(text)):
        if text[index] == '>':
            strength += int(text[index + 1])
            text_after_explosion += text[index]
            strength -= 1
        elif strength == 0 and text[index].isalpha():
            text_after_explosion += text[index]
        elif strength > 0 and text[index].isalpha():
            strength -= 1
    return text_after_explosion

text = input()
print(explosion(text))
