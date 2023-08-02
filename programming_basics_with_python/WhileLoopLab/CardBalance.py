total_payment = 0

while True:
    payment = input()

    if payment == 'NoMoreMoney':
        break

    payment = float(payment)

    if payment > 0:
        total_payment += payment
        print(f'Increase: {payment:.2f}')
    else:
        print('Invalid operation!')
        break

print(f'Total: {total_payment:.2f}')

