prime_sum, non_prime_sum = 0, 0

while True:
    command = input()

    if command == 'stop':
        break

    number = int(command)

    if number < 0:
        print(f'Number is negative.')
    if number > 1:
        for i in range(2, int(number / 2) + 1):
            if (number % i) == 0:
                non_prime_sum += number
                break
        else:
            prime_sum += number
    elif number == 1:
        non_prime_sum += number

print(f"Sum of all prime numbers is: {prime_sum}")
print(f"Sum of all non prime numbers is: {non_prime_sum}")



