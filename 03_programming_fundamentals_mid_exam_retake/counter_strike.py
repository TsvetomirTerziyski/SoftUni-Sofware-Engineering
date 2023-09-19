initial_energy = int(input())
command = input()
won_battles = 0
break_cycle = False

while command != 'End of battle':
    if initial_energy >= int(command):
        won_battles += 1
        if won_battles % 3 == 0:
            initial_energy += won_battles
        initial_energy -= int(command)
    else:
        break_cycle = True
        break

    command = input()

if break_cycle:
    print(f"Not enough energy! Game ends with {won_battles} won battles and {initial_energy} energy")
else:
    print(f"Won battles: {won_battles}. Energy left: {initial_energy}")
