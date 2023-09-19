pirate_ship_status = [int(i) for i in input().split('>')]
warship_status = [int(i) for i in input().split('>')]
maximum_health_for_section = int(input())
break_cycle = False

while True:
    command = input().split()

    if command[0] == 'Retire':
        print(f"Pirate ship status: {sum(pirate_ship_status)}\nWarship status: {sum(warship_status)}")
        break

    elif command[0] == 'Fire':
        index, damage = int(command[1]), int(command[2])

        if index in range(len(warship_status)):
            warship_status[index] -= damage
            if warship_status[index] <= 0:
                print("You won! The enemy ship has sunken.")
                break

    elif command[0] == 'Defend':
        start_index, end_index, damage = int(command[1]), int(command[2]), int(command[3])

        if start_index in range(len(pirate_ship_status)) and end_index in range(len(pirate_ship_status)):
            for index in range(start_index, end_index + 1):
                pirate_ship_status[index] -= damage
                if pirate_ship_status[index] <= 0:
                    break_cycle = True
                    break
        if break_cycle:
            print("You lost! The pirate ship has sunken.")
            break

    elif command[0] == 'Repair':
        index, health = int(command[1]), int(command[2])

        if index in range(len(pirate_ship_status)):
            if pirate_ship_status[index] + health > maximum_health_for_section:
                add_health = health - (pirate_ship_status[index] + health - maximum_health_for_section)
                pirate_ship_status[index] += add_health
            else:
                pirate_ship_status[index] += health

    elif command[0] == 'Status':
        sections_for_repair = []

        for section in pirate_ship_status:
            if section < maximum_health_for_section * 0.2:
                sections_for_repair.append(section)
        print(f"{len(sections_for_repair)} sections need repair.")
