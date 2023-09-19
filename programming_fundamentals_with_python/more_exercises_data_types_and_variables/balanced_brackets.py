n = int(input())
last_symbol = ''
balanced = 0
unbalanced = 0

for _ in range(n):
    symbol = input()

    if symbol != '(' and symbol != ')':
        continue
    elif last_symbol == '(' and symbol == ')':
        balanced += 1
    elif symbol == ')' and (last_symbol == '' or last_symbol == ')'):
        unbalanced += 1

    last_symbol = symbol

if balanced > unbalanced:
    print('BALANCED')
else:
    print('UNBALANCED')
