budget = int(input())
total_price = 0

while True:
    command = input()

    if command == 'End':
        print("You bought everything needed.")
        break

    product_price = int(command)

    if budget < product_price:
        print("You went in overdraft!")
        break

    total_price += product_price
    budget -= product_price



