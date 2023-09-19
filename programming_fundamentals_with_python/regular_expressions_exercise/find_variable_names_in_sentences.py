import re

text = input()
pattern = r'\b_([A-Za-zd]+)\b'
matches = re.findall(pattern, text)

print(','.join(matches))
