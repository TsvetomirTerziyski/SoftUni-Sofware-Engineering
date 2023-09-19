input_list = input().split()
input_list_integer = list(map(int, input_list))

filtered = filter(lambda x: x % 2 == 0, input_list_integer)
print(list(filtered))
