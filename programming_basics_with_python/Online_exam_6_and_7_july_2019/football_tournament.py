team_name = input()
played_matches = int(input())

counter, wins, draws, losses = 0, 0, 0, 0

for _ in range(played_matches):

    if played_matches == 0:
        break

    result = input()

    if played_matches > 0:
        if result == 'W':
            counter += 3
            wins += 1
        elif result == 'D':
            counter += 1
            draws += 1
        elif result == 'L':
            losses += 1

if played_matches > 0:
    print(f"{team_name} has won {counter} points during this season.")
    print("Total stats:")
    print(f"## W: {wins}")
    print(f"## D: {draws}")
    print(f"## L: {losses}")
    print(f"Win rate: {(wins/played_matches)*100:.2f}%")
elif played_matches == 0:
    print(f"{team_name} hasn't played any games during this season.")



