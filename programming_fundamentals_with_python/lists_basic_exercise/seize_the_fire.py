fire_and_cell = input().split('#')
amount_of_water = int(input())
high = range(81, 126)
medium = range(51, 81)
low = range(1, 51)
effort = 0  # Its value is equal to 25% of the cell's value
total_fire = 0  # Its value is equal to the sum of the cells
cells = []

for index in range(len(fire_and_cell)):
    fire, cell = fire_and_cell[index].split('=')

    if fire == 'High ' and int(cell) in high and amount_of_water >= int(cell):
        amount_of_water -= int(cell)
        effort += 0.25 * int(cell)
        total_fire += int(cell)

    elif fire == 'Medium ' and int(cell) in medium and amount_of_water >= int(cell):
        amount_of_water -= int(cell)
        effort += 0.25 * int(cell)
        total_fire += int(cell)

    elif fire == 'Low ' and int(cell) in low and amount_of_water >= int(cell):
        amount_of_water -= int(cell)
        effort += 0.25 * int(cell)
        total_fire += int(cell)
    else:
        continue

    cells.append(cell)

print('Cells:')
for element in cells:
    print(f' -{element}')
print(f"Effort: {effort:.2f}")
print(f"Total Fire: {total_fire}")
