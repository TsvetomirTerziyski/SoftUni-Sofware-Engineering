groups = int(input())

Musala = 0
Monblan = 0
Kilimandjaro = 0
K2 = 0
Everest = 0
total_people = 0

for _ in range(groups):
    people_in_group = int(input())

    total_people += people_in_group

    if people_in_group <= 5:
        Musala += people_in_group
    elif 6 <= people_in_group <= 12:
        Monblan += people_in_group
    elif 13 <= people_in_group <= 25:
        Kilimandjaro += people_in_group
    elif 26 <= people_in_group <= 40:
        K2 += people_in_group
    else:
        Everest += people_in_group

print(f'{Musala/total_people*100:.2f}%')
print(f'{Monblan/total_people*100:.2f}%')
print(f'{Kilimandjaro/total_people*100:.2f}%')
print(f'{K2/total_people*100:.2f}%')
print(f'{Everest/total_people*100:.2f}%')



