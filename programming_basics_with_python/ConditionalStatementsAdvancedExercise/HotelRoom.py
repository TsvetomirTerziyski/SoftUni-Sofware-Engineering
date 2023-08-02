month = input()
nights_count = int(input())

room_type = ''
studio_price = 0
apartment_price = 0

if (7 < nights_count <= 14) and (month == 'May' or month == 'October'):
    studio_price = nights_count * (50 - (50 * 0.05))
    apartment_price = nights_count * 65
elif (nights_count > 14) and (month == 'May' or month == 'October'):
    studio_price = nights_count * (50 - (50 * 0.30))
    apartment_price = nights_count * (65 - (65 * 0.10))
elif (7 < nights_count <= 14) and (month == 'June' or month == 'September'):
    studio_price = nights_count * 75.20
    apartment_price = nights_count * 68.70
elif (nights_count > 14) and (month == 'June' or month == 'September'):
    studio_price = nights_count * (75.20 - (75.20 * 0.20))
    apartment_price = nights_count * (68.70 - (68.70 * 0.10))
elif (7 < nights_count <= 14) and (month == 'July' or month == 'August'):
    studio_price = nights_count * 76
    apartment_price = nights_count * 77
elif (nights_count > 14) and (month == 'July' or month == 'August'):
    studio_price = nights_count * 76
    apartment_price = nights_count * (77 - (77 * 0.10))

print(f'Apartment: {apartment_price:.2f} lv.')
print(f'Studio: {studio_price:.2f} lv.')
