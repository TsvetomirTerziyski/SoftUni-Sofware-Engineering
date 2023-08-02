chicken_menu = int(input())
fish_menu = int(input())
vegetarian_menu = int(input())

chicken_menu_price = 10.35
fish_menu_price = 12.40
vegetarian_menu_price = 8.15

price = (chicken_menu * chicken_menu_price) + (fish_menu * fish_menu_price) + (vegetarian_menu * vegetarian_menu_price)
dessert_price = 0.2 * price
delivery = 2.50
total_price = price + dessert_price + delivery

print(f'{total_price:.2f}')



