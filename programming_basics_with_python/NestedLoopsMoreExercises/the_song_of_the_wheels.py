M = int(input())

counter = 0
flag = False
password = ''

for a in range(1,10):
    for b in range(1,10):
        for c in range(1,10):
            for d in range(1,10):

                if (a * b) + (c * d) == M:
                    if a < b:
                        if c > d:

                            counter += 1

                            if counter == 4:
                                password = f'{a}{b}{c}{d}'
                                flag = True

                            print(f'{a}{b}{c}{d}', end=' ')
            if flag:
                continue
        if flag:
            continue
    if flag:
        continue
if flag:
    print()
    print(f'Password: {password}')
else:
    print()
    print('No!')






