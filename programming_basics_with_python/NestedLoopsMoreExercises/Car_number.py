first_number = int(input())
last_number = int(input())

for n1 in range(first_number, last_number + 1):
    for n2 in range(first_number, last_number + 1):
        for n3 in range(first_number, last_number + 1):
            for n4 in range(first_number, last_number + 1):

                number = f'{n1}{n2}{n3}{n4}'

                if (n1 % 2 == 0 and n4 % 2 != 0) or (n1 % 2 != 0 and n4 % 2 == 0):
                    if n1 > n4:
                        if (n2 + n3) % 2 == 0:
                            print(number, end=' ')
