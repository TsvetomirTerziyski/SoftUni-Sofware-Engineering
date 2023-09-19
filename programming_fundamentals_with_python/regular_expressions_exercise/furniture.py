import re

furniture_info = input()
total_cost = 0
furniture = []
pattern = r'>>([A-Za-z]+)<<(\d+\.?\d*)!(\d+)'

while furniture_info != 'Purchase':
    matches = re.search(pattern, furniture_info)
    if matches:
        furniture_name, price, quantity = matches.groups()
        furniture.append(furniture_name)
        total_cost += float(price) * int(quantity)
    furniture_info = input()

print('Bought furniture:')
for f in furniture:
    print(f)
print(f'Total money spend: {total_cost:.2f}')
