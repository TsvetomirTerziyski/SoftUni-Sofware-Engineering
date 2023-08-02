n1, n2 = int(input()), int(input())

for n in range(n1,n2+1):
    even_sum, odd_sum = 0, 0
    for index, digit in enumerate(str(n)):

        if index % 2 == 0:
            even_sum += int(digit)
        else:
            odd_sum += int(digit)

    if even_sum == odd_sum:
        print(n, end=' ')
