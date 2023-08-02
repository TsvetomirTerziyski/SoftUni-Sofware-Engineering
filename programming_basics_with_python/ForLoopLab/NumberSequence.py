import sys

n = int(input())

max_number: int = -sys.maxsize
min_number: int = sys.maxsize

for num in range(n):
    numbers: int = int(input())

    if numbers > max_number:
        max_number = numbers

    if numbers < min_number:
        min_number = numbers

print(f'Max number: {max_number}\nMin number: {min_number}')
