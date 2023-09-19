input_list = input().split()
stock = {}

for index in range(0, len(input_list), 2):
    product = input_list[index]
    quantity = int(input_list[index + 1])

    stock[product] = quantity

products_to_search = input().split()

for product in products_to_search:
    if product in stock:
        print(f'We have {stock[product]} of {product} left')
    else:
        print(f"Sorry, we don't have {product}")
