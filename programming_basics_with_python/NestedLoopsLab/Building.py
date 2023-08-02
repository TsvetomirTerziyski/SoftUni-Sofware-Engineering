floors = int(input())
rooms_per_floor = int(input())
flat_name = ''

for current_floor in range(floors, 0, -1):
    for current_room in range(rooms_per_floor):
        if current_floor == floors:
            flat_name = f'L{current_floor}{current_room}'
        elif current_floor % 2 == 0:
            flat_name = f'O{current_floor}{current_room}'
        elif current_floor % 2 == 1:
            flat_name = f'A{current_floor}{current_room}'

        print(flat_name, end=' ')
    print()



