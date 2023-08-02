male_clients = int(input())
female_clients = int(input())
tables = int(input())

table_counter = 0

for n_male in range(1, male_clients + 1):
    for n_female in range(1, female_clients + 1):

        table_counter += 1

        if table_counter > tables:
            break
        else:
            print(f'({n_male} <-> {n_female})', end=' ')