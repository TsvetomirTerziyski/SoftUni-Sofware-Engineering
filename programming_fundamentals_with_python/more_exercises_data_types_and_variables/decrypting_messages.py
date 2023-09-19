key = int(input())
n = int(input())
final = ''

for _ in range(n):
    letter = input()

    next_letter = ord(letter) + key
    next_letter_char = chr(next_letter)
    final += next_letter_char

print(final)
