number = int(input())

isValid = True

if 100 <= number <= 200 or number == 0:
    isValid = True
else:
    isValid = False
    print('invalid')
