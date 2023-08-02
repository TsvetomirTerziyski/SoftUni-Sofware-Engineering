wanted_profit = float(input())

income = 0

while income < wanted_profit:
    cocktail_name = input()

    if cocktail_name == 'Party!':
        print(f"We need {wanted_profit - income:.2f} leva more.")
        break

    cocktails = int(input())

    cocktail_price = len(cocktail_name)

    cocktail_price *= cocktails

    if cocktail_price % 2 != 0:
        cocktail_price *= 0.75

    income += cocktail_price

    if income >= wanted_profit:
        print('Target acquired.')

print(f"Club income - {income:.2f} leva.")
