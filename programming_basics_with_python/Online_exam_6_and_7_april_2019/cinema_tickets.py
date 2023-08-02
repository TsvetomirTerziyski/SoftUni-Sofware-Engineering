student, standard, kid = 0, 0, 0

while True:
    command = input()

    if command == 'Finish':
        break

    movie_name = command

    capacity = int(input())

    sold_tickets = 0

    while sold_tickets < capacity:
        ticket_type = input()

        if ticket_type == 'End':
            break

        if ticket_type == 'student':
            student += 1
        elif ticket_type == 'standard':
            standard += 1
        elif ticket_type == 'kid':
            kid += 1

        sold_tickets += 1

    print(f"{movie_name} - {sold_tickets/capacity*100:.2f}% full.")


total_tickets = student + standard + kid

print(f"Total tickets: {total_tickets}")
print(f"{student/total_tickets*100:.2f}% student tickets.")
print(f"{standard/total_tickets*100:.2f}% standard tickets.")
print(f"{kid/total_tickets*100:.2f}% kids tickets.")
