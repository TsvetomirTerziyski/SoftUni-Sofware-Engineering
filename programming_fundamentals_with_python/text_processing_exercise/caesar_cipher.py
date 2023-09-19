def encrypted_text(text):
    encrypted = ''
    for char in text:
        encrypted += chr(ord(char) + 3)
    return encrypted


text = input()
print(encrypted_text(text))
