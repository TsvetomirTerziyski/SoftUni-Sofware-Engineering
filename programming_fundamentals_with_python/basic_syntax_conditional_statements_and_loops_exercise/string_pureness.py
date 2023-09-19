number_of_strings_in_the_cycle = int(input())
pure = False
not_pure = False

for _ in range(number_of_strings_in_the_cycle):
    string = input()

    for symbol in string:
        if symbol == ',' or symbol == '.' or symbol == '_':
            not_pure = True
            break
    else:
        pure = True

    if pure:
        print(f'{string} is pure.')
        pure = False
    else:
        print(f'{string} is not pure!')