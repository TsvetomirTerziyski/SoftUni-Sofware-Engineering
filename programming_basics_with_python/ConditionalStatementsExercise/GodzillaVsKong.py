film_budget = float(input())
number_of_extras = int(input())
clothes_for_one = float(input())

total_price = 0
decor = film_budget * 0.10
clothes_for_all_discounted = 0

if number_of_extras > 150:
    clothes_for_all = clothes_for_one * number_of_extras
    clothes_for_all_discounted =clothes_for_all * 0.90
    total_price = clothes_for_all_discounted + decor
else:
    clothes_for_all = clothes_for_one * number_of_extras
    total_price = clothes_for_all + decor

if total_price > film_budget:
    print(f'Not enough money!')
    print(f'Wingard needs {total_price - film_budget:.2f} leva more.')
else:
    print(f'Action!')
    print(f'Wingard starts filming with {film_budget - total_price:.2f} leva left.')
