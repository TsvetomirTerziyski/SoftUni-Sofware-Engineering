username = input()
password = input()

data = ''

while data != password:
    data = input()

    if data == password:
        print(f'Welcome {username}!')