import re

input_string = input()
pattern = r'([=/])([A-Z][A-Za-z]{2,})\1'
matches = re.findall(pattern, input_string)
valid_destinations = []
travel_points = 0

for match in matches:
    valid_destinations.append(match[1])
    travel_points += len(match[1])
print(f"Destinations: {', '.join(valid_destinations)}")
print(f"Travel Points: {travel_points}")
