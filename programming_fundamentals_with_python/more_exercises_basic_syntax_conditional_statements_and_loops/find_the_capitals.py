input_text = input()

list_from_input = list(input_text)
lst = []

for index, digit in enumerate(list_from_input):
    if digit == digit.upper() and digit.isalpha():
        lst.append(index)

print(lst)
