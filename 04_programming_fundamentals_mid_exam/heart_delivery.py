input_list = input().split('@')
input_list_integers = [int(i) for i in input_list]

command = input().split()
last_position = 0

while command[0] != 'Love!':
    length = int(command[1])
    for index in range(len(input_list_integers)):
        index = last_position

        if index + length in range(len(input_list_integers)):
            index = index + length
            if input_list_integers[index] == 0:
                last_position = index
                print(f"Place {index} already had Valentine's day.")
                break
            else:
                last_position = index
                input_list_integers[index] -= 2

                if input_list_integers[index] == 0:
                    print(f"Place {index} has Valentine's day.")
                    break
                else:
                    break
        elif index + length not in range(len(input_list_integers)):
            index = 0
            if input_list_integers[index] == 0:
                last_position = index
                print(f"Place {index} already had Valentine's day.")
                break
            else:
                last_position = index
                input_list_integers[index] -= 2
                if input_list_integers[index] == 0:
                    print(f"Place {index} has Valentine's day.")
                    break
                else:
                    break

    command = input().split()

print(f"Cupid's last position was {last_position}.")
if sum(input_list_integers) == 0:
    print(f"Mission was successful.")
else:
    not_celebrated_list = [i for i in input_list_integers if i > 0]
    print(f"Cupid has failed {len(not_celebrated_list)} places.")
