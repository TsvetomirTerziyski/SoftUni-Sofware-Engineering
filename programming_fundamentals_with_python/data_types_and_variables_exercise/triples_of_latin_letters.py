n = int(input())

for n1 in range(n):
    for n2 in range(n):
        for n3 in range(n):
            print(f'{chr(97+n1)}{chr(97+n2)}{chr(97+n3)}')
