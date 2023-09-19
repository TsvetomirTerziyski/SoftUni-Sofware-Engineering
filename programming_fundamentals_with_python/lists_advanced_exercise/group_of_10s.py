from math import ceil

list_integers = [int(num) for num in input().split(', ')]
max_value = max(list_integers)
age_groups = ceil(max_value / 10)
years = 10
list_of_age_groups = []

for age_group in range(1, age_groups + 1):
    list_of_age_groups = [num for num in list_integers if num in range(years - 9, years + 1)]
    print(f"Group of {years}'s: {list_of_age_groups}")
    years += 10
