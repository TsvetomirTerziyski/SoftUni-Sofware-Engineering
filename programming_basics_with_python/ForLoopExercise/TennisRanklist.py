from math import floor

tournaments = int(input())
beginning_points = int(input())

points = 0
wins = 0

for _ in range(tournaments):
    place = input()

    if place == 'W':
        points += 2000
        wins += 1
    elif place == 'F':
        points += 1200
    elif place == 'SF':
        points += 720

print(f'Final points: {beginning_points + points}')
print(f'Average points: {floor(points/tournaments)}')
print(f'{(wins/tournaments)*100:.2f}%')


