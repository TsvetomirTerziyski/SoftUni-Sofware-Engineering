n = int(input())

for number in range(1,n+1):
    list_of_digits = [int(num) for num in str(number)]
    if sum(list_of_digits) == 5 or sum(list_of_digits) == 7 or sum(list_of_digits) == 11:
        print(f'{number} -> {True}')
    else:
        print(f'{number} -> {False}')
