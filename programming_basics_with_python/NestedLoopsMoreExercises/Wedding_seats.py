last_sector = input()
rows_first_sector = int(input())
odd_row_seats = int(input())

first_seat = 97
seats_counter = 0

for sector in range(ord('A'),ord(last_sector)+1):
    for rows in range(1, rows_first_sector + 1):

        if rows % 2 != 0:
            for seats in range(first_seat, (first_seat + odd_row_seats)):
                print(f'{chr(sector)}{rows}{chr(seats)}')
                seats_counter += 1
        elif rows % 2 == 0:
            for seats in range(first_seat, (first_seat + odd_row_seats + 2)):
                print(f'{chr(sector)}{rows}{chr(seats)}')
                seats_counter += 1

        if rows_first_sector == rows:
            rows_first_sector += 1

print(seats_counter)