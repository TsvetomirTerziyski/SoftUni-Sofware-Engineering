input_list = input().split(', ')
sorted_list = sorted(input_list, key=lambda x: (-len(x), x))
print(sorted_list)
