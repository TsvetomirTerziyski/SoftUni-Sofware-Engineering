force_dict = {}
bool = False

while True:
    command = input()

    if ' | ' in command:
        command = command.split(' | ')
        force_side, force_user = command[0], command[1]

        if force_side not in force_dict.keys() and force_user not in force_dict.values():
            force_dict[force_side] = []

        for side, users in force_dict.items():
            if force_user not in users:
                bool = True
            else:
                bool = False
                break
        if bool:
            force_dict[force_side].append(force_user)

    elif ' -> ' in command:
        command = command.split(' -> ')
        force_user, force_side = command[0], command[1]

        if force_side not in force_dict.keys() and force_user not in force_dict.values():
            force_dict[force_side] = []

        for side, users in force_dict.items():
            if force_user not in users:
                bool = True
            else:
                if force_user in users:
                    deleted = force_dict[side].pop(users.index(force_user))
                    force_dict[force_side].append(deleted)
                    print(f"{deleted} joins the {force_side} side!")
                    bool = False
                break
        if bool:
            force_dict[force_side].append(force_user)
            print(f"{force_user} joins the {force_side} side!")

    elif command == 'Lumpawaroo':
        for side, user in force_dict.items():
            if len(user) > 0:
                print(f"Side: {side}, Members: {len(user)}")
            for member in user:
                print(f"! {member}")
        break
