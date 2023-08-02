best_score = 0
winner_name = ''

while True:
    command = input()

    if command == 'Stop':
        break

    current_points = 0

    name = command

    for n in name:

        number = int(input())

        if number == ord(n):
            current_points += 10
        else:
            current_points += 2

        if current_points >= best_score:
            best_score = current_points
            winner_name = name

print(f"The winner is {winner_name} with {best_score} points!")











