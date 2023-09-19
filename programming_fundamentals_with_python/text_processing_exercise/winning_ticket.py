def check_ticket(ticket):
    if len(ticket) != 20:
        return "invalid ticket"

    left_part = ticket[:10]
    right_part = ticket[10:]

    for winning_symbol in winning_symbols:
        for uninterrupted_match_length in range(10, 5, -1):
            winning_rep = winning_symbol * uninterrupted_match_length
            if winning_rep in left_part and winning_rep in right_part:
                if uninterrupted_match_length == 10:
                    return f'ticket "{ticket}" - {uninterrupted_match_length}{winning_symbol} Jackpot!'
                return f'ticket "{ticket}" - {uninterrupted_match_length}{winning_symbol}'
    return f'ticket "{ticket}" - no match'


tickets = [ticket.strip() for ticket in input().split(', ')]
winning_symbols = ['@', '#', '$', '^']

for ticket in tickets:
    print(check_ticket(ticket))
