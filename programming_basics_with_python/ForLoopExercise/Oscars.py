actor_name = input()
academy_points = float(input())
n = int(input())

max_points = 1250.5

for _ in range(n):
    evaluative_name = input()
    evaluative_points = float(input())

    academy_points += len(evaluative_name) * evaluative_points / 2

    if academy_points >= max_points:
        print(f'Congratulations, {actor_name} got a nominee for leading role with {academy_points:.1f}!')
        break
else:
    print(f'Sorry, {actor_name} you need {max_points - academy_points:.1f} more!')






