input_list = input().split(' ')
n = int(input())
input_list_numbers = []
final_list = []

for element in input_list:
    input_list_numbers.append(int(element))

for _ in range(n):
    input_list_numbers.remove(min(input_list_numbers))

for element in input_list_numbers:
    final_list.append(str(element))

print((', ').join(final_list))
