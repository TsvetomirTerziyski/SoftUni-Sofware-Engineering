dungeons_rooms = input().split('|')
initial_health = 100
initial_bitcoins = 0

for room in dungeons_rooms:
    current_room = dungeons_rooms.index(room)+1
    room = room.split()
    command, amount = room[0], int(room[1])

    if command == 'potion':
        initial_health += amount
        if initial_health > 100:
            amount = amount - (initial_health - 100)
            initial_health = 100
        print(f"You healed for {amount} hp.")
        print(f"Current health: {initial_health} hp.")
    elif command == 'chest':
        initial_bitcoins += amount
        print(f"You found {amount} bitcoins.")
    else:
        initial_health -= amount
        if initial_health > 0:
            print(f"You slayed {command}.")
        else:
            print(f"You died! Killed by {command}." )
            best_room = current_room
            print(f"Best room: {best_room}")
            break

if initial_health > 0:
    print("You've made it!")
    print(f"Bitcoins: {initial_bitcoins}")
    print(f"Health: {initial_health}")
