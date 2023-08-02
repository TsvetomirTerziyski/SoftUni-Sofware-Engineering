nylon = int(input())
paint = int(input())
thinner = int(input())
hours = int(input())

nylon_price = (nylon + 2) * 1.50
paint_price = (paint + (0.1 * paint)) * 14.50
thinner_price = thinner * 5
bags_price = 0.40

material_total_price = nylon_price + paint_price + thinner_price + bags_price
work_price = (0.3 * material_total_price) * hours
total_price = material_total_price + work_price

print(total_price)







