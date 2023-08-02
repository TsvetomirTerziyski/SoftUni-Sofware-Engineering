flowers_type = input()
flowers_count = int(input())
budget = int(input())
price = 0

if flowers_type == 'Roses':
    price = flowers_count * 5
elif flowers_type == 'Dahlias':
    price = flowers_count * 3.80
elif flowers_type == 'Tulips':
    price = flowers_count * 2.80
elif flowers_type == 'Narcissus':
    price = flowers_count * 3
elif flowers_type == 'Gladiolus':
    price = flowers_count * 2.50

if flowers_count > 80 and flowers_type == 'Roses':
    price = 0.90 * price
elif flowers_count > 90 and flowers_type == 'Dahlias':
    price = 0.85 * price
elif flowers_count > 80 and flowers_type == 'Tulips':
    price = 0.85 * price
elif flowers_count < 120 and flowers_type == 'Narcissus':
    price = 1.15 * price
elif flowers_count < 80 and flowers_type == 'Gladiolus':
    price = 1.20 * price

if budget >= price:
    print(f'Hey, you have a great garden with {flowers_count} {flowers_type} and {budget - price:.2f} leva left.')
else:
    print(f'Not enough money, you need {price - budget:.2f} leva more.')