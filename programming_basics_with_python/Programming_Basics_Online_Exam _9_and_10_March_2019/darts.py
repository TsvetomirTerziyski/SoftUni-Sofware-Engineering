player_name = input()

starting_points = 301
successful_shots = 0
unsuccessful_shots = 0

while True:
    command = input()

    if command == 'Retire':
        print(f"{player_name} retired after {unsuccessful_shots} unsuccessful shots.")
        break

    sector = command
    points = int(input())

    current_points = 0

    if sector == 'Single':
        current_points = points
    elif sector == 'Double':
        current_points = points * 2
    elif sector == 'Triple':
        current_points = points * 3

    if starting_points >= current_points:
        successful_shots += 1
        starting_points -= current_points
    else:
        unsuccessful_shots += 1

    if starting_points == 0:
        print(f"{player_name} won the leg with {successful_shots} shots.")
        break
