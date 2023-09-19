import re

text = input()
pattern = r'([@#])([A-Za-z]{3,})\1{2}([A-Za-z]{3,})\1'
matches = re.findall(pattern, text)
word_pairs = 0
mirror_words = []

for match in matches:
    word_pairs += 1
    if match[1] == match[2][::-1]:
        mirror_words.append(f'{match[1]} <=> {match[2]}')

if word_pairs == 0:
    print("No word pairs found!")
else:
    print(f"{word_pairs} word pairs found!")
if len(mirror_words) == 0:
    print("No mirror words!")
else:
    print("The mirror words are:")
    print(', '.join(mirror_words))
