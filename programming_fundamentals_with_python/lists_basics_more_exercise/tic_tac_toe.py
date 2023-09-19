first_row = input().split(' ')
second_row = input().split(' ')
third_row = input().split(' ')

player = 1
player_name = 'First'
win = False

while player < 3:
    player = str(player)
    line = [player, player, player]

    if line == first_row or line == second_row or line == third_row:    # If the line is on the row
        win = True

    for column in range(3):
        if player == first_row[column] and player == second_row[column] and player == third_row[column]:    # If the line is on the column
            win = True

    if player == first_row[0] and player == second_row[1] and player == third_row[2]:    # Left diagonal win
        win = True
    elif player == first_row[2] and player == second_row[1] and player == third_row[0]:    # Right diagonal win
        win = True
    if win:
        print(f"{player_name} player won")
        break
    player_name = 'Second'
    player = int(player) + 1
else:
    print("Draw!")
