number_of_lines = int(input())
capacity = 255

for n in range(number_of_lines):
    current_liters = int(input())

    if current_liters > capacity:
        print('Insufficient capacity!')
        continue

    capacity -= current_liters

print(f'{255-capacity}')

