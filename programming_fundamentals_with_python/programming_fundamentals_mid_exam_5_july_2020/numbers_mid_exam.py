input_list = [int(i) for i in input().split()]
average_value = round(sum(input_list) / len(input_list),2)
list_above_average = []

for element in input_list:
    if average_value < 0:
        if element > average_value:
            list_above_average.append(element)
    else:
        if element > average_value:
            list_above_average.append(element)

while len(list_above_average) > 5:
    list_above_average.sort(reverse=True)
    list_above_average.pop()

if len(list_above_average) > 0:
    list_above_average.sort(reverse=True)
    print(' '.join(str(i) for i in list_above_average))
else:
    print('No')
