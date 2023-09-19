a = int(input())
b = int(input())

print('Before:')
print(f'a = {a}')
print(f'b = {b}')

temp_var = a
a = b
b = temp_var

print('After:')
print(f'a = {a}')
print(f'b = {b}')
