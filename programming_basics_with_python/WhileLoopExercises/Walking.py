aim_steps = 10000
steps_walked = 0

while steps_walked < aim_steps:
    steps = input()

    if steps == 'Going home':
        steps_walked += int(input())
        break

    steps_walked += int(steps)

if steps_walked >= aim_steps:
    print("Goal reached! Good job!")
    print(f'{steps_walked - aim_steps} steps over the goal!')
else:
    print(f'{aim_steps - steps_walked} more steps to reach goal.')






