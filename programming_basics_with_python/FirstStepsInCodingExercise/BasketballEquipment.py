annual_tax = int(input())

basketball_shoes_price = annual_tax - (0.4 * annual_tax)
basketball_jersey_price = basketball_shoes_price - (0.2 * basketball_shoes_price)
basketball_ball_price = basketball_jersey_price / 4
basketball_accessories_price = basketball_ball_price / 5

final_price = annual_tax + basketball_shoes_price + basketball_jersey_price + basketball_ball_price + basketball_accessories_price

print(final_price)