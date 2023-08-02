max_hundreds = int(input())
max_tens = int(input())
max_singles = int(input())

for n1 in range(2, max_hundreds + 1, 2):
    for n2 in range(2, max_tens + 1):
        for n3 in range(2, max_singles + 1, 2):

            if n2 == 2 or n2 == 3 or n2 == 5 or n2 == 7:

                print(n1, end=' ')
                print(n2, end=' ')
                print(n3)




