n = int(input())
list_of_positive_numbers = []
list_of_negative_numbers = []

for _ in range(n):
    number = int(input())

    if number >= 0:
        list_of_positive_numbers.append(number)
    else:
        list_of_negative_numbers.append(number)

print(list_of_positive_numbers)
print(list_of_negative_numbers)
print(f"Count of positives: {len(list_of_positive_numbers)}")
print(f'Sum of negatives: {sum(list_of_negative_numbers)}')
