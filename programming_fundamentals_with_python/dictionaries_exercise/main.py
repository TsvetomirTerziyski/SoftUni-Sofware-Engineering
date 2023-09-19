sides_db = {}

def find_user(username, collection):
    group = ''
    exists = 'no'
    for key, value in collection.items():
        if username in value:
            group = key
            exists = 'yes'
            break
    return group, exists


while True:
    command = input()
    if command == 'Lumpawaroo':
        break

    if ' | ' in command:
        pair = command.split(' | ')
        side = pair[0]
        user = pair[1]

        group, exists = find_user(user, sides_db)

        if exists == 'no':
            if not side in sides_db:
                sides_db[side] = [user]
            else:
                sides_db[side].append(user)
        else:
            pass

    elif ' -> ' in command:
        pair = command.split(' -> ')
        user = pair[0]
        side = pair[1]

        group, exists = find_user(user, sides_db)

        if exists == 'no':
            if not side in sides_db:
                sides_db[side] = [user]
            else:
                sides_db[side].append(user)
            print(f"{user} joins the {side} side!")
        else:
            sides_db[group].remove(user)
            if not side in sides_db:
                sides_db[side] = [user]
            else:
                sides_db[side].append(user)
            print(f"{user} joins the {side} side!")

for key, value in sides_db.items():
    value = sorted(value)
    sides_db[key] = value

sides_db = sorted(sides_db.items(), key=lambda x: (-(len(x[1])),x[0]))

for item in sides_db:
    if len(item[1]) > 0:
        print(f"Side: {item[0]}, Members: {len(item[1])}")
        [print(f"! {user}") for user in item[1]]
