number_of_commands = int(input())
registered_users = {}

for current_command in range(number_of_commands):
    command = input().split()

    if command[0] == 'register':
        username, license_plate_number = command[1], command[2]

        if username not in registered_users:
            registered_users[username] = license_plate_number
            print(f"{username} registered {license_plate_number} successfully")
        else:
            print(f"ERROR: already registered with plate number {license_plate_number}")
    elif command[0] == 'unregister':
        username = command[1]

        if username not in registered_users:
            print(f"ERROR: user {username} not found")
        else:
            del registered_users[username]
            print(f"{username} unregistered successfully")

for username, license_plate_number in registered_users.items():
    print(f"{username} => {license_plate_number}")
