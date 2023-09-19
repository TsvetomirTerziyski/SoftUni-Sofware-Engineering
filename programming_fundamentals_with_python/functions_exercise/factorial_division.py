def factorial_division(n1, n2):
    first_factorial = n1
    second_factorial = n2

    for n_one in range(n1 - 1, 0, -1):
        first_factorial *= n_one
    for n_two in range(n2 - 1, 0, -1):
        second_factorial *= n_two

    return f'{first_factorial / second_factorial:.2f}'


first_number = int(input())
second_number = int(input())
print(factorial_division(first_number, second_number))
