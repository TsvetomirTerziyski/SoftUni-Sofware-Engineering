days_to_stay = int(input())
room_type = input()
feedback = input()

price = 0
nights = days_to_stay - 1

if days_to_stay < 10:
    if room_type == 'room for one person':
        price = nights * 18
    elif room_type == 'apartment':
        price = (nights * 25) - (nights * 25 * 0.3)
    elif room_type == 'president apartment':
        price = (nights * 35) - (nights * 35 * 0.1)
elif 10 <= days_to_stay <= 15:
    if room_type == 'room for one person':
        price = nights * 18
    elif room_type == 'apartment':
        price = (nights * 25) - (nights * 25 * 0.35)
    elif room_type == 'president apartment':
        price = (nights * 35) - (nights * 35 * 0.15)
elif days_to_stay > 15:
    if room_type == 'room for one person':
        price = nights * 18
    elif room_type == 'apartment':
        price = (nights * 25) - (nights * 25 * 0.50)
    elif room_type == 'president apartment':
        price = (nights * 35) - (nights * 35 * 0.20)

if feedback == 'positive':
    price += price * 0.25
elif feedback == 'negative':
    price -= price * 0.10

print(f'{price:.2f}')