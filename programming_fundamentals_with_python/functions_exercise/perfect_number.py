def perfect_number(num):
    proper_divisors_sum = 0
    for n in range(1, num):
        if num % n == 0:
            proper_divisors_sum += n

    if proper_divisors_sum == num:
        return "We have a perfect number!"
    else:
        return "It's not so perfect."


number = int(input())
print(perfect_number(number))
