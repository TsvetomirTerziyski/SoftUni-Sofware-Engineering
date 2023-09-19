input_string = input().split()
inverted_list = []

for index, digit in enumerate(input_string):
    inverted_list.append(-int(digit))

print(inverted_list)
