total = int(input()) * int(input())
piece_counter = 0

while True:
    pieces = input()

    if pieces == "STOP":
        print(f'{total - piece_counter} pieces are left.')
        break

    piece_counter += int(pieces)
    
    if piece_counter > total:
        print(f'No more cake left! You need {piece_counter - total} pieces more.')
        break
