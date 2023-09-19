budget = float(input())
one_kg_flour_price = float(input())

one_pack_of_eggs_price = one_kg_flour_price * 0.75
one_liter_milk_price = one_kg_flour_price * 1.25

cooking_recipe_for_one_easter_bread = one_pack_of_eggs_price + one_kg_flour_price + (one_liter_milk_price / 4)
colored_eggs = 0
number_of_loaves = 0
current_count_of_loaves = 0

while True:
    if budget < cooking_recipe_for_one_easter_bread:
        break

    current_count_of_loaves += 1
    colored_eggs += 3

    if current_count_of_loaves % 3 == 0:
        colored_eggs -= current_count_of_loaves - 2

    number_of_loaves += 1
    budget -= cooking_recipe_for_one_easter_bread

print(f"You made {number_of_loaves} loaves of Easter bread! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.")







