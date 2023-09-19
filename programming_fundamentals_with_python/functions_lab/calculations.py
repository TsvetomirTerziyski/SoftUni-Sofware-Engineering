operator = input()
n1 = int(input())
n2 = int(input())


def calculator(a, b, operation):
    if operation == 'multiply':
        return a * b
    elif operation == 'divide':
        return int(a / b)
    elif operation == 'add':
        return a + b
    elif operation == 'subtract':
        return a - b


print(calculator(n1, n2, operator))
