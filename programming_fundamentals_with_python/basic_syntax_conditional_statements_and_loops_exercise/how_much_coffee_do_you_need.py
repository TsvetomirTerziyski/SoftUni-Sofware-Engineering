coffees = 0

while True:
    command = input()

    if command == 'END':
        break

    string = command

    if string == 'coffee' or string == 'dog' or string == 'cat' or string == 'movie' or string == 'coding':
        coffees += 1
    elif string == 'COFFEE' or string == 'DOG' or string == 'CAT' or string == 'MOVIE' or string == 'CODING':
        coffees += 2
    else:
        continue

if coffees > 5:
    print("You need extra sleep")
else:
    print(coffees)

