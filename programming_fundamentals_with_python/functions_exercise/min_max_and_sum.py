input_list = input().split()
input_list_integers = []

for element in input_list:
    input_list_integers.append(int(element))

maximum = max(input_list_integers)
minimum = min(input_list_integers)
summed = sum(input_list_integers)

print(f"The minimum number is {minimum}")
print(f"The maximum number is {maximum}")
print(f"The sum number is: {summed}")
