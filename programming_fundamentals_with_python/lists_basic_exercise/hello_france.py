input_list = input().split('|')
start_budget = float(input())
budget_left = start_budget
train_ticket = 150
max_price_clothes = 50
max_price_shoes = 35
max_price_accessories = 20.50
list_with_new_prices = []   # In this list add bought items with a 40% markup
is_enough = False

for index in range(len(input_list)):
    type_price = input_list[index].split('->')
    price = float(type_price[1])

    if (type_price[0] == 'Clothes' and price > max_price_clothes) \
        or (type_price[0] == 'Shoes' and price > max_price_shoes) \
        or (type_price[0] == 'Accessories' and price > max_price_accessories):
        continue

    if budget_left >= price:
        if type_price[0] == 'Clothes' and 0 < price <= 50:
            budget_left -= price
            price *= 1.4
            list_with_new_prices.append(price)
        elif type_price[0] == 'Shoes' and 0 < price <= 35:
            budget_left -= price
            price *= 1.4
            list_with_new_prices.append(price)
        elif type_price[0] == 'Accessories' and 0 < price <= 20.50:
            budget_left -= float(price)
            price *= 1.4
            list_with_new_prices.append(price)
    else:
        continue

if budget_left + sum(list_with_new_prices) >= train_ticket:
    is_enough = True

for element in list_with_new_prices:
    print(f'{element:.2f}', end=' ')
print()
print(f"Profit: {(budget_left + sum(list_with_new_prices)) - start_budget:.2f}")

if is_enough:
    print("Hello, France!")
else:
    print("Not enough money.")
