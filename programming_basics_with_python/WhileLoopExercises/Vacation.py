money_needed = float(input())
available_money = float(input())

days_counter = 0
spend_counter = 0


while True:
    action = input()  # spend or save
    saved_or_spend_price = float(input())

    days_counter += 1

    if action == 'spend':
        spend_counter += 1
        if saved_or_spend_price > available_money:
            available_money = 0
        else:
            available_money -= saved_or_spend_price

        if spend_counter == 5:
            print("You can't save the money.")
            print(f'{days_counter}')
            break

    elif action == 'save':
        available_money += saved_or_spend_price
        spend_counter = 0
        if available_money >= money_needed:
            print(f'You saved the money for {days_counter} days.')
            break
