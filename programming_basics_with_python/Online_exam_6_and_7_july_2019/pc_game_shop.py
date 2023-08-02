n = int(input())

h_counter = 0
f_counter = 0
overwatch_counter = 0
others_counter = 0

for _ in range(n):
    name = input()

    if name == 'Hearthstone':
        h_counter += 1
    elif name == 'Fornite':
        f_counter += 1
    elif name == 'Overwatch':
        overwatch_counter += 1
    else:
        others_counter += 1

print(f"Hearthstone - {(h_counter/n)*100:.2f}%")
print(f"Fornite - {(f_counter/n)*100:.2f}%")
print(f"Overwatch - {(overwatch_counter/n)*100:.2f}%")
print(f"Others - {(others_counter/n)*100:.2f}%")
