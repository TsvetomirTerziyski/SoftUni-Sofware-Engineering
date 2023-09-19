input_list = [i.lower() for i in input().split()]

dictionary = {}

for i in input_list:
    if i in dictionary:
        dictionary[i] += 1
    else:
        dictionary[i] = 1

for k, v in dictionary.items():
    if v % 2 != 0:
        print(k, end=' ')
