start_points = int(input())

bonus = 0

if start_points <= 100:
    bonus = 5
elif 100 < start_points <= 1000:
    bonus = start_points * 0.20
else:
    bonus = start_points * 0.10

if start_points % 2 == 0:
    bonus += 1
elif start_points % 10 == 5:
    bonus += 2

print(bonus)
print(start_points + bonus)