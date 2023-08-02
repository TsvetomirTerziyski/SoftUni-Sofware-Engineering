budget = float(input())
season = input()

destination = ''
money_spend = 0
vacation_place = ''

if budget <= 100:
    destination = 'Bulgaria'
    if season == 'summer':
        vacation_place = 'Camp'
        money_spend = budget * 0.3
    elif season == 'winter':
        vacation_place = 'Hotel'
        money_spend = budget * 0.7
elif budget <= 1000:
    destination = 'Balkans'
    if season == 'summer':
        vacation_place = 'Camp'
        money_spend = budget * 0.4
    elif season == 'winter':
        vacation_place = 'Hotel'
        money_spend = budget * 0.8
elif budget > 1000:
    destination = 'Europe'
    vacation_place = 'Hotel'
    if season == 'summer' or season == 'winter':
        money_spend = budget * 0.9

print(f"Somewhere in {destination}")
print(f"{vacation_place} - {money_spend:.2f}")




