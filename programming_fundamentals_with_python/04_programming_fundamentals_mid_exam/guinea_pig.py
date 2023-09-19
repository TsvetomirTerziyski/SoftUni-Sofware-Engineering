food_quantity_grams = float(input())*1000
hay_quantity_grams = float(input())*1000
cover_quantity_grams = float(input())*1000
guinea_weight_grams = float(input())*1000
is_not_enough = False
period_days = 30

for day in range(1,31):
    food_quantity_grams -= 300
    if day % 2 == 0:
        hay_quantity_grams -= food_quantity_grams * 0.05
    if day % 3 == 0:
        cover_quantity_grams -= guinea_weight_grams / 3
    if food_quantity_grams <= 0 or hay_quantity_grams <= 0 or cover_quantity_grams <= 0:
        is_not_enough = True
        break

if is_not_enough:
    print("Merry must go to the pet store!")
else:
    print(f"Everything is fine! Puppy is happy! Food: {food_quantity_grams/1000:.2f}, "
          f"Hay: {hay_quantity_grams/1000:.2f}, Cover: {cover_quantity_grams/1000:.2f}.")
