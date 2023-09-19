input_list = input().split(', ')
number_of_beggars = int(input())
sum_list = []
number_input_list = []

for element in input_list:
    number_input_list.append(int(element))

for beggar in range(number_of_beggars):
    sum_list.append(sum(number_input_list[beggar::number_of_beggars]))

print(sum_list)
