while True:
    command = input()

    if command == 'Welcome!':
        print("Welcome to Hogwarts.")
        break

    if command == 'Voldemort':
        print("You must not speak of that name!")
        break

    name = command

    if len(name) < 5:
        print(f"{name} goes to Gryffindor.")
    elif len(name) == 5:
        print(f"{name} goes to Slytherin.")
    elif len(name) == 6:
        print(f"{name} goes to Ravenclaw.")
    else:
        print(f"{name} goes to Hufflepuff.")