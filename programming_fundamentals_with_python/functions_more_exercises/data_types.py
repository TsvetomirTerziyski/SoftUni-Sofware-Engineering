def operation_with_the_number(string, num):
    if string == 'int':
        return f'{float(num) * 2:.0f}'
    elif string == 'real':
        return f'{float(num) * 1.5:.2f}'
    elif string == 'string':
        return f'${num}$'


input_string = input()
number = input()

result = operation_with_the_number(input_string, number)
print(result)
