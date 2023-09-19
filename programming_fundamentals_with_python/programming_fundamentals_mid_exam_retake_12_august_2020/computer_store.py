price_without_taxes = 0

while True:
    command = input()

    if command == 'special' or command == 'regular':
        break

    part_price = float(command)

    if part_price < 0:
        print("Invalid price!")
        continue

    price_without_taxes += part_price

taxes = price_without_taxes * 0.2

if command == 'special':
    final_price = price_without_taxes + taxes - ((price_without_taxes + taxes) * 0.1)
else:
    final_price = price_without_taxes + taxes

if price_without_taxes == 0:
    print("Invalid order!")
else:
    print(f"Congratulations you've just bought a new computer!\n "
    f"Price without taxes: {price_without_taxes:.2f}$\n "
    f"Taxes: {taxes:.2f}$\n"
    f"-----------\n"
    f"Total price: {final_price:.2f}$")
