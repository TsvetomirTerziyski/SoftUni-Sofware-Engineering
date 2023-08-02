holiday_price = float(input())

puzzles = int(input())
talking_dolls = int(input())
teddy_bears = int(input())
minions = int(input())
trucks = int(input())

puzzle_price = 2.60
doll_price = 3
teddy_bear_price = 4.10
minion_price = 8.20
truck_price = 2

toy_count = puzzles + talking_dolls + teddy_bears + minions + trucks
total_price = (puzzles * puzzle_price) \
              + (talking_dolls * doll_price) \
              + (teddy_bears * teddy_bear_price) \
              + (minions * minion_price) \
              + (trucks * truck_price)

if toy_count >= 50:
    total_price *= 0.75

total_price *= 0.90

if total_price >= holiday_price:
    print(f'Yes! {total_price - holiday_price:.2f} lv left.')
else:
    print(f'Not enough money! {holiday_price - total_price:.2f} lv needed.')