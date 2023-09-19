import re

text = input()
pattern = r'(#|\|)([A-Za-z\s]+)\1(\d{2,2}/\d{2,2}/\d{2,2})\1(\d{1,5})\1'
matches = re.finditer(pattern, text)
total_calories = 0
items = []

for match in matches:
    item_name, expiration_date, calories = match.group(2), match.group(3), int(match.group(4))
    total_calories += int(match.group(4))
    items.append([item_name, expiration_date, calories])

print(f"You have food to last you for: {total_calories//2000} days!")

for item in items:
    name_of_item, date, cals = item[0], item[1], item[2]
    print(f"Item: {name_of_item}, Best before: {date}, Nutrition: {cals}")
