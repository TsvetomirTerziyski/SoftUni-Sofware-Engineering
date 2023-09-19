num = int(input())
prime = False

if num > 1:
    for i in range(2,num):
        if (num % i) == 0:
            prime = False
            break
    else:
        prime = True
else:
    prime = False

print(prime)
