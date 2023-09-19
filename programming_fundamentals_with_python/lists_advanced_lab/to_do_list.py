def to_do_list():
    lst = []

    while True:
        command = input()

        if command == 'End':
            break

        lst.append(command)

    sorted_list = sorted(lst, key=lambda x: int(x.split('-')[0]))
    result_sorted_list = [command.split('-')[1] for command in sorted_list]
    return result_sorted_list


print(to_do_list())
