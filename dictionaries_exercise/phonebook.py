phonebook = {}

while True:
    input_info = input().split('-')

    if input_info[0].isnumeric():
        searches = int(input_info[0])
        break

    name, number = input_info[0], input_info[1]

    phonebook[name] = number

for search in range(searches):
    searched_name = input()

    if searched_name in phonebook.keys():
        print(f'{searched_name} -> {phonebook[searched_name]}')
    else:
        print(f"Contact {searched_name} does not exist.")
