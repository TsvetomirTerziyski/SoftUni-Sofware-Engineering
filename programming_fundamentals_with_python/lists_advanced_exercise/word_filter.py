def even_length(lst):
    list_even = [x for x in lst if len(x) % 2 == 0]
    return list_even


input_list = input().split(' ')
even_list = even_length(input_list)
for element in even_list:
    print(element)
