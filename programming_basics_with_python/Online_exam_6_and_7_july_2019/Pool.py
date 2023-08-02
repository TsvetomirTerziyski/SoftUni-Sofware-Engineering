from math import ceil

n_people = int(input())
entrance_fee = float(input())
sunbed_price = float(input())
umbrella_price = float(input())

total_entrance = n_people * entrance_fee

total_sunbed = (ceil(n_people * 0.75)) * sunbed_price
total_umbrella = (ceil(n_people * 0.50)) * umbrella_price

final_price = total_entrance + total_sunbed + total_umbrella

print(f'{final_price:.2f} lv.')