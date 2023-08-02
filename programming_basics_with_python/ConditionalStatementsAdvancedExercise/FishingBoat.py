budget = int(input())
season = input()
fishers_count = int(input())

price = 0
total_price = 0

if fishers_count <= 6:
    if season == 'Spring':
        price = 3000
        total_price = price * 0.9
    elif season == 'Summer' or season == 'Autumn':
        price = 4200
        total_price = price * 0.9
    elif season == 'Winter':
        price = 2600
        total_price = price * 0.9
elif 7 <= fishers_count <= 11:
    if season == 'Spring':
        price = 3000
        total_price = price * 0.85
    elif season == 'Summer' or season == 'Autumn':
        price = 4200
        total_price = price * 0.85
    elif season == 'Winter':
        price = 2600
        total_price = price * 0.85
elif fishers_count >= 12:
    if season == 'Spring':
        price = 3000
        total_price = price * 0.75
    elif season == 'Summer' or season == 'Autumn':
        price = 4200
        total_price = price * 0.75
    elif season == 'Winter':
        price = 2600
        total_price = price * 0.75

if fishers_count % 2 == 0 and not season == 'Autumn':
    total_price *= 0.95

if budget > total_price:
    print(f'Yes! You have {budget - total_price:.2f} leva left.')
else:
    print(f'Not enough money! You need {total_price - budget:.2f} leva.')



