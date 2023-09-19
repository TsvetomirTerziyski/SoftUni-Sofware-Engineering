number_of_snowballs = int(input())
highest_value = 0
biggest_weight = 0
best_time = 0
best_quality = 0

for current_snowball in range(number_of_snowballs):
    weight = int(input())
    time_needed = int(input())
    quality = int(input())

    snowball_value = (weight / time_needed) ** quality

    if snowball_value > highest_value:
        highest_value = snowball_value
        biggest_weight = weight
        best_time = time_needed
        best_quality = quality

print(f"{biggest_weight} : {best_time} = {int(highest_value)} ({best_quality})")
