def train_list_manipulator(lst):
    people = 0
    index = 0
    while True:
        command = input().split()

        if command[0] == 'End':
            print(lst)
            break

        elif command[0] == 'add':
            people = int(command[1])
            lst[-1] += people

        elif command[0] == 'insert':
            index = int(command[1])
            people = int(command[2])
            lst[index] += people

        elif command[0] == 'leave':
            index = int(command[1])
            people = int(command[2])
            lst[index] -= people


wagons = int(input())
train = [0] * wagons

train_list_manipulator(train)
