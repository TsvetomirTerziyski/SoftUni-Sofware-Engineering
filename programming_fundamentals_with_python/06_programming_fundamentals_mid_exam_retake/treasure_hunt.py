def loot(chest, loot_items_list):
    for element_to_add in loot_items_list:
        if element_to_add not in chest:
            chest.insert(0, element_to_add)
    return chest


def drop(chest, index_to_drop):
    if len(chest) > 0:
        if index_to_drop in range(len(chest)):
            chest.append(chest.pop(index_to_drop))
    return chest


def steal(chest, count_of_items):
    deleted_items = []
    if len(chest) > 0:
        if count_of_items > len(chest):
            while len(chest) > 0:
                deleted_items.append(chest.pop(0))
        else:
            for index_to_remove in range(count_of_items, 0, -1):
                deleted_items.append(chest.pop(-index_to_remove))

        print(', '.join(deleted_items))
    return chest

treasure_chest = input().split('|')
sum_items_length = 0
average_treasure_gain = 0

command = input().split()

while command[0] != 'Yohoho!':
    if command[0] == 'Loot':
        loot_items = []
        for element in range(1, len(command)):
            loot_items.append(command[element])
        treasure_chest = loot(treasure_chest, loot_items)
    elif command[0] == 'Drop':
        index = int(command[1])
        treasure_chest = drop(treasure_chest, index)
    elif command[0] == 'Steal':
        count = int(command[1])
        treasure_chest = steal(treasure_chest, count)

    command = input().split()

for item in treasure_chest:
    sum_items_length += len(item)

if len(treasure_chest) == 0:
    print("Failed treasure hunt.")
else:
    average_treasure_gain = sum_items_length / len(treasure_chest)
    print(f"Average treasure gain: {average_treasure_gain:.2f} pirate credits.")
