days = int(input())
hours = int(input())

total_price_all_days = 0
counter = 0

for d in range(1, days + 1):
    counter += 1
    price = 0
    for h in range(1, hours + 1):

        if d % 2 == 0 and h % 2 != 0:
            price += 2.50
        elif d % 2 != 0 and h % 2 == 0:
            price += 1.25
        else:
            price += 1

    print(f'Day: {counter} - {price:.2f} leva')
    total_price_all_days += price

print(f"Total: {total_price_all_days:.2f} leva")