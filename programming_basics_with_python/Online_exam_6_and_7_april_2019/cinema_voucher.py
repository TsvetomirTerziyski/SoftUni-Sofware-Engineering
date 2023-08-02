voucher = int(input())

ticket_counter, others = 0, 0

while True:
    command = input()

    if command == 'End':
        break
    if voucher <= 0:
        break
    product = command

    first_char = product[0]
    second_char = product[1]

    if len(product) > 8:
        if ord(first_char) + ord(second_char) <= voucher:
            voucher -= (ord(first_char) + ord(second_char))
            ticket_counter += 1
        else:
            break
    elif len(product) <= 8:
        if ord(first_char) <= voucher:
            voucher -= ord(first_char)
            others += 1
        else:
            break

print(f"{ticket_counter}")
print(f"{others}")