quantity_of_decorations = int(input())
days_left_until_christmas = int(input())

ornament_set_price = 2
tree_skirt_price = 5
tree_garland_price = 3
tree_lights_price = 15
christmas_spirit = 0
total_cost = 0

for day in range(1,days_left_until_christmas+1):
    if day % 11 == 0:
        quantity_of_decorations += 2
    if day % 2 == 0:
        total_cost += (quantity_of_decorations * ornament_set_price)
        christmas_spirit += 5
    if day % 3 == 0:
        total_cost += (quantity_of_decorations * tree_skirt_price) + (quantity_of_decorations * tree_garland_price)
        christmas_spirit += 13
    if day % 5 == 0:
        total_cost += (quantity_of_decorations * tree_lights_price)
        christmas_spirit += 17
        if day % 3 == 0 and day % 5 == 0:
            christmas_spirit += 30
    if day % 10 == 0:
        christmas_spirit -= 20
        total_cost += tree_skirt_price + tree_garland_price + tree_lights_price
    if day % 10 == 0 and day == days_left_until_christmas:
        christmas_spirit -= 30

print(f"Total cost: {total_cost}")
print(f"Total spirit: {christmas_spirit}")
