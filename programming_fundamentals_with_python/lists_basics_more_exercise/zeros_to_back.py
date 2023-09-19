input_list = input().split(', ')
final_list = []

for element in input_list:

    if element == '0':
        removed_element = input_list.remove(element)
        input_list.append(element)

for element in input_list:
    final_list.append(int(element))

print(final_list)
