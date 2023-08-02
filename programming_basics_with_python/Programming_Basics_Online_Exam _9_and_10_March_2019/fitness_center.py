n = int(input())

workout, protein = 0, 0
back, chest, legs, core, protein_shake, protein_bar = 0, 0, 0, 0, 0, 0

for _ in range(n):
    fitness_members = n

    activity = input()

    if activity == 'Back':
        back += 1
    elif activity == 'Chest':
        chest += 1
    elif activity == 'Legs':
        legs += 1
    elif activity == 'Abs':
        core += 1
    elif activity == 'Protein shake':
        protein_shake += 1
    elif activity == 'Protein bar':
        protein_bar += 1

    if activity == 'Back' or activity == 'Chest' or activity == 'Legs' or activity == 'Abs':
        workout += 1
    elif activity == 'Protein shake' or activity == 'Protein bar':
        protein += 1

print(f"{back} - back")
print(f"{chest} - chest")
print(f"{legs} - legs")
print(f"{core} - abs")
print(f"{protein_shake} - protein shake")
print(f"{protein_bar} - protein bar")
print(f"{(workout / n)*100:.2f}% - work out")
print(f"{(protein / n)*100:.2f}% - protein")