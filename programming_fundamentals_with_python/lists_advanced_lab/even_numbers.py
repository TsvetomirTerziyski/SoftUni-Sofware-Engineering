def even_numbers_indices(lst):
    indices_list = []
    for index, digit in enumerate(lst):
        if int(digit) % 2 == 0:
            indices_list.append(int(index))
    return indices_list


input_list = input().split(', ')
result = even_numbers_indices(input_list)
print(result)
