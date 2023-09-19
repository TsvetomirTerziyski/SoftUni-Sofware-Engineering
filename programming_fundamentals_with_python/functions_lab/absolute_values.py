input_list = input().split()
input_list_floating = list(map(float, input_list))
abs_list = []

for element in input_list_floating:
    abs_list.append(abs(element))

print(abs_list)
