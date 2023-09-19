age = int(input())

type_of_drink = ''

if age <= 14:
    type_of_drink = 'drink toddy'
elif age <= 18:
    type_of_drink = 'drink coke'
elif age <= 21:
    type_of_drink = 'drink beer'
else:
    type_of_drink = 'drink whisky'

print(type_of_drink)