messages_send = int(input())

for _ in range(messages_send):
    number = int(input())

    if number == 88:
        print('Hello')
    elif number == 86:
        print('How are you?')
    elif number > 88:
        print('Bye.')
    else:
        print('GREAT!')