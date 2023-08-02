student, standard, kids = 0, 0, 0

while True:
    movie_name = input()

    if movie_name == 'Finish':
        break

    capacity = int(input())

    sold_tickets = 0

    while sold_tickets < capacity:
        ticket_type = input()

        if ticket_type == 'End':
            break

        if ticket_type == 'student':
            sold_tickets += 1
            student += 1
        elif ticket_type == 'standard':
            sold_tickets += 1
            standard += 1
        elif ticket_type == 'kid':
            sold_tickets += 1
            kids += 1

    print(f"{movie_name} - {sold_tickets/capacity*100:.2f}% full.")

total_tickets = student + standard + kids

print(f"Total tickets: {total_tickets}")
print(f'{student/total_tickets*100:.2f}% student tickets.')
print(f"{standard/total_tickets*100:.2f}% standard tickets.")
print(f"{kids/total_tickets*100:.2f}% kids tickets.")