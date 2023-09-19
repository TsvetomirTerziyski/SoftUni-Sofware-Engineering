input_list = input().split()
bakery = {}

for index in range(0, len(input_list), 2):
    key = input_list[index]
    value = int(input_list[index + 1])

    bakery[key] = value

print(bakery)
