result_one = input()
result_two = input()
result_three = input()

win = 0
lost = 0
draw = 0

if ord(result_one[0]) > ord(result_one[2]):
    win += 1
elif ord(result_one[0]) < ord(result_one[2]):
    lost += 1
else:
    draw += 1

if ord(result_two[0]) > ord(result_two[2]):
    win += 1
elif ord(result_two[0]) < ord(result_two[2]):
    lost += 1
else:
    draw += 1

if ord(result_three[0]) > ord(result_three[2]):
    win += 1
elif ord(result_three[0]) < ord(result_three[2]):
    lost += 1
else:
    draw += 1

print(f"Team won {win} games.")
print(f"Team lost {lost} games.")
print(f"Drawn games: {draw}")