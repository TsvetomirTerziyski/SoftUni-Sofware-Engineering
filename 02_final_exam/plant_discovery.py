def rate(plant_rarity_dict, plant_type, rating_to_add):
    if plant_type in plant_rarity_dict.keys():
        plant_rarity_dict[plant_type][1].append(int(rating_to_add))
    else:
        print('error')
    return plant_rarity_dict


def update(plant_dict, plant_type, new_plant_rarity):
    if plant_type in plant_dict.keys():
        plant_dict[plant_type][0] = new_plant_rarity
    else:
        print('error')
    return plant_dict


def reset(plant_dict, plant_type):
    if plant_type in plant_dict.keys():
        plant_dict[plant_type][1] = []
    else:
        print('error')
    return plant_dict


number_of_lines = int(input())
plant_rarity = {}

for _ in range(number_of_lines):
    plant_info = input().split('<->')

    plant, rarity = plant_info[0], plant_info[1]

    if plant not in plant_rarity.keys():
        plant_rarity[plant] = [rarity, []]
    plant_rarity[plant] = [rarity, []]

command = input().split(': ')

while command[0] != 'Exhibition':
    if command[0] == 'Rate':
        plant, rating = command[1].split(' - ')
        plant_rating = rate(plant_rarity, plant, rating)
    elif command[0] == 'Update':
        plant, new_rarity = command[1].split(' - ')
        plant_rarity = update(plant_rarity, plant, new_rarity)
    elif command[0] == 'Reset':
        plant = command[1]
        plant_rarity = reset(plant_rarity, plant)

    command = input().split(': ')

print('Plants for the exhibition:')
for plant, info in plant_rarity.items():
    if len(info[1]) > 0:
        print(f'- {plant}; Rarity: {info[0]}; Rating: {sum(info[1])/len(info[1]):.2f}')
    else:
        print(f'- {plant}; Rarity: {info[0]}; Rating: {0.00:.2f}')
