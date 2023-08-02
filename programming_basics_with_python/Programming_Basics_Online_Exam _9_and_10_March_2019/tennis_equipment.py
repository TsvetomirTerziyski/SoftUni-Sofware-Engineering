from math import floor, ceil

tennis_rocket_price = float(input())
tennis_rockets = int(input())
sneakers = int(input())

total_rocket_price = tennis_rockets * tennis_rocket_price

sneakers_price = tennis_rocket_price / 6

total_sneakers_price = sneakers_price * sneakers

the_rest_of_the_equipment = (total_rocket_price + total_sneakers_price) * 0.2

total_price_full_equipment = total_rocket_price + total_sneakers_price + the_rest_of_the_equipment

print(f"Price to be paid by Djokovic {floor(total_price_full_equipment / 8)}")
print(f"Price to be paid by sponsors {ceil((total_price_full_equipment * 7) / 8)}")
