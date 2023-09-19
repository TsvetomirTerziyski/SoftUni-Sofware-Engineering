stock = {}
while True:
    command = input().split(': ')

    if 'statistics' in command:
        print('Products in stock:')
        for key, value in stock.items():
            print(f'- {key}: {value}')
        print(f'Total Products: {len(stock)}')
        print(f'Total Quantity: {sum(stock.values())}')
        break

    key, value = command[0], command[1]

    if key in stock:
        stock[key] += int(value)
    else:
        stock[key] = int(value)
