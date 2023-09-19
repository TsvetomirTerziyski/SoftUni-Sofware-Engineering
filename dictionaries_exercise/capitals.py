country_names = input().split(', ')
capitals = input().split(', ')

dictionary = {country_names[index]: capitals[index] for index in range(len(country_names))}

for country, capital in dictionary.items():
    print(f'{country} -> {capital}')
