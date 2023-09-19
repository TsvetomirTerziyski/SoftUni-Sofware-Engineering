items_dict = {"shards": 0, "fragments": 0, "motes": 0}
obtained = False
input_list = input().split()

while not obtained:

    for index in range(0, len(input_list), 2):
        quantity = int(input_list[index])
        material = input_list[index+1].lower()

        if material not in items_dict:
            items_dict[material] = 0
        items_dict[material] += quantity

        if items_dict['shards'] >= 250:
            items_dict['shards'] -= 250
            obtained = True
            print(f'Shadowmourne obtained!')
        elif items_dict['fragments'] >= 250:
            items_dict['fragments'] -= 250
            obtained = True
            print(f'Valanyr obtained!')
        elif items_dict['motes'] >= 250:
            items_dict['motes'] -= 250
            obtained = True
            print(f'Dragonwrath obtained!')
        if obtained:
            break
    if obtained:
        break
    input_list = input().split()

for key, value in items_dict.items():
    print(f'{key}: {value}')
