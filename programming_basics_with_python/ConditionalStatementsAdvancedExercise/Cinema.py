projection_type = input()
rows = int(input())
columns = int(input())

hall_capacity = rows * columns
total_price = 0

if projection_type == 'Premiere':
    total_price = hall_capacity * 12
elif projection_type == 'Normal':
    total_price = hall_capacity * 7.50
elif projection_type == 'Discount':
    total_price = hall_capacity * 5

print(f'{total_price:.2f} leva')

