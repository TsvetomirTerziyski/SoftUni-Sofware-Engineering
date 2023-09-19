product = input()
quantity = int(input())


def total_price(product, quantity):
    if product == 'coffee':
        price = quantity * 1.5
        return f'{price:.2f}'
    elif product == 'water':
        price = quantity * 1
        return f'{price:.2f}'
    elif product == 'coke':
        price = quantity * 1.4
        return f'{price:.2f}'
    elif product == 'snacks':
        price = quantity * 2
        return f'{price:.2f}'


print(total_price(product, quantity))
