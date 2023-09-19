def interpreted_message(input_message):
    while True:
        command = input()

        if command == 'Reveal':
            print(f"You have a new text message: {input_message}")
            break
        else:
            command = command.split(':|:')

        if command[0] == 'InsertSpace':
            index = command[1]
            input_message = input_message[:int(index)] + ' ' + input_message[int(index):]
            print(input_message)
        elif command[0] == 'Reverse':
            if command[1] in input_message:
                input_message = input_message.replace(command[1], '', 1)
                input_message = input_message + command[1][::-1]
                print(input_message)
            else:
                print('error')
        elif command[0] == 'ChangeAll':
            input_message = input_message.replace(command[1], command[2])
            print(input_message)


message = input()
interpreted_message(message)
