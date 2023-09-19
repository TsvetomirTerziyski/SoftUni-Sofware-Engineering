orders = {}
command = input().split()

while command[0] != 'buy':
    name, price, quantity = command[0], float(command[1]), int(command[2])

    if name not in orders:
        orders[name] = [price, quantity]
    else:
        orders[name][0] = price
        orders[name][1] += quantity

    command = input().split()

for order, total in orders.items():
    total_price = total[0] * total[1]
    print(f'{order} -> {total_price:.2f}')
