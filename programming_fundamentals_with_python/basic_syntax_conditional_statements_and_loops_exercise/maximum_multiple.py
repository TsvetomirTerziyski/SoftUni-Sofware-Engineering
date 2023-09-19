divisor = int(input())
boundary = int(input())

for n in range(boundary, 0, -1):
    if n % divisor == 0:
        if n <= boundary:
            print(n)
            break

