def urgent(list_to_use, item_to_add):
    is_not_in_list = True
    for index in range(len(list_to_use)):
        if list_to_use[index] == item_to_add:
            is_not_in_list = False
            break
    if is_not_in_list:
        list_to_use.insert(0, item_to_add)
    return list_to_use

def unnecessary(list_to_use, item_to_remove):
    is_in_list = False
    for index in range(len(list_to_use)):
        if list_to_use[index] == item_to_remove:
            is_in_list = True
            break
    if is_in_list:
        list_to_use.remove(item_to_remove)
    return list_to_use

def correct(list_to_use, item_old_name, item_new_name):
    old_name_is_in_list = False
    for index in range(len(list_to_use)):
        if list_to_use[index] == old_item:
            old_name_is_in_list = True
            break
    if old_name_is_in_list:
        old_name_index = list_to_use.index(item_old_name)
        list_to_use[old_name_index] = item_new_name
    return list_to_use

def rearrange(list_to_use, item_to_manipulate):
    item_to_manipulate_is_in_list = False
    for index in range(len(list_to_use)):
        if list_to_use[index] == item_to_manipulate:
            item_to_remove_index = index
            item_to_manipulate_is_in_list = True
            break
    if item_to_manipulate_is_in_list:
        removed_item = list_to_use.pop(item_to_remove_index)
        list_to_use.append(removed_item)
    return list_to_use

input_list = input().split('!')

while True:
    command = input().split()

    if command[0] == 'Go':
        break

    elif command[0] == 'Urgent':
        item = command[1]
        input_list = urgent(input_list, item)
    elif command[0] == 'Unnecessary':
        item = command[1]
        input_list = unnecessary(input_list, item)
    elif command[0] == 'Correct':
        old_item, new_item = command[1], command[2]
        input_list = correct(input_list, old_item, new_item)
    elif command[0] == 'Rearrange':
        item = command[1]
        input_list = rearrange(input_list, item)

print(', '.join(input_list))
