import re

text = input()
pattern = r'w{3}.[A-Za-z0-9-]+[.a-z]+$'
valid = []

while text:
    match = re.findall(pattern, text)
    if match:
        valid.append(match[0])
    text = input()

for m in valid:
    print(m)
