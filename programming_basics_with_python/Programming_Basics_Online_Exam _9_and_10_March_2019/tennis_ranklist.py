from math import floor

tournaments = int(input())
starting_points = int(input())

wins = 0
points_without_starting_points = 0

for _ in range(tournaments):
    tournament_stage_achieved = input()

    if tournament_stage_achieved == 'W':
        starting_points += 2000
        points_without_starting_points += 2000
        wins += 1
    elif tournament_stage_achieved == 'F':
        points_without_starting_points += 1200
        starting_points += 1200
    elif tournament_stage_achieved == 'SF':
        points_without_starting_points += 720
        starting_points += 720

print(f"Final points: {starting_points}")
print(f"Average points: {floor(points_without_starting_points / tournaments)}")
print(f"{(wins / tournaments) * 100:.2f}%")