def collect(items_list, item_to_add):
    if item_to_add not in items_list:
        items_list.append(item_to_add)
    return items_list


def drop(items_list, item_to_drop):
    if item_to_drop in items_list:
        items_list.remove(item_to_drop)
    return items_list


def combine_items(items_list, old, new):
    if old in items_list:
        old_index = items_list.index(old)
        items_list.insert(old_index+1, new)
    return items_list

def renew(items_list, item_to_manipulate):
    if item_to_manipulate in items_list:
        item_to_manipulate_index = items_list.index(item_to_manipulate)
        removed = items_list.pop(item_to_manipulate_index)
        items_list.append(removed)
    return items_list


collecting_items_list = input().split(', ')

command = input().split(" - ")

while command[0] != 'Craft!':
    if command[0] == 'Collect':
        item = command[1]
        collecting_items_list = collect(collecting_items_list, item)
    elif command[0] == 'Drop':
        item = command[1]
        collecting_items_list = drop(collecting_items_list, item)
    elif command[0] == 'Combine Items':
        old_item, new_item = command[1].split(':')
        collecting_items_list = combine_items(collecting_items_list, old_item, new_item)
    elif command[0] == 'Renew':
        item = command[1]
        collecting_items_list = renew(collecting_items_list, item)

    command = input().split(' - ')

print(', '.join(collecting_items_list))
