working_day_events = input().split('|')
initial_energy = 100
initial_coins = 100
current_energy = 100
is_successful = True
gained_energy = 0

for element in working_day_events:
    event_ingredient, number = element.split('-')

    if event_ingredient == 'rest':
        gained_energy = min(int(number), initial_energy - current_energy)
        current_energy += gained_energy
        print(f"You gained {abs(gained_energy)} energy.")
        print(f"Current energy: {current_energy}.")

    elif event_ingredient == 'order':
        current_energy -= 30
        if current_energy >= 0:
            initial_coins += int(number)
            print(f"You earned {int(number)} coins.")
        else:
            current_energy += 30 + 50
            print("You had to rest!")

    else:
        initial_coins -= int(number)
        if initial_coins >= 0:
            print(f"You bought {event_ingredient}.")
        else:
            print(f"Closed! Cannot afford {event_ingredient}.")
            is_successful = False
            break

if is_successful:
    print("Day completed!")
    print(f"Coins: {initial_coins}")
    print(f"Energy: {current_energy}")
