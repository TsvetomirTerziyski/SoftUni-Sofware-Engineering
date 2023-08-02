first_player, second_player = input(), input()

first_player_points, second_player_points = 0, 0
winner = ''
winner_points = 0

while True:
    command = input()

    if command == 'End of game':
        print(f"{first_player} has {first_player_points} points")
        print(f"{second_player} has {second_player_points} points")
        break

    first_player_card = int(command)
    second_player_card = int(input())

    if first_player_card > second_player_card:
        first_player_points += first_player_card - second_player_card
    elif first_player_card < second_player_card:
        second_player_points += second_player_card - first_player_card

    if first_player_card == second_player_card:
        first_player_card = int(input())
        second_player_card = int(input())

        if first_player_card > second_player_card:
            winner_points = first_player_points
            winner = first_player
        elif first_player_card < second_player_card:
            winner = second_player
            winner_points = second_player_points

        print("Number wars!")
        print(f"{winner} is winner with {winner_points} points")
        break
