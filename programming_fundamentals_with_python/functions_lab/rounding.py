input_list = input().split()
input_list_floating = list(map(float, input_list))
rounded_list = []

for element in input_list_floating:
    rounded_list.append(round(element))

print(rounded_list)
