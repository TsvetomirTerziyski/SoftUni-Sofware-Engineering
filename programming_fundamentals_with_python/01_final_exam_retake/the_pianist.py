def add_piece(piece_to_add, composer_to_add, key_to_add, pieces_dict):
    if piece_to_add in pieces_dict:
        print(f"{piece_to_add} is already in the collection!")
    else:
        pieces_dict[piece_to_add] = [composer_to_add, key_to_add]
        print(f"{piece_to_add} by {composer_to_add} in {key_to_add} added to the collection!")


def remove_piece(piece_to_remove, pieces_dict):
    if piece_to_remove in pieces_dict:
        del pieces_dict[piece_to_remove]
        print(f"Successfully removed {piece_to_remove}!")
    else:
        print(f"Invalid operation! {piece_to_remove} does not exist in the collection.")


def change_key(piece_to_change, key_to_change, pieces_dict):
    if piece_to_change in pieces_dict:
        pieces_dict[piece_to_change][1] = key_to_change
        print(f"Changed the key of {piece_to_change} to {key_to_change}!")
    else:
        print(f"Invalid operation! {piece_to_change} does not exist in the collection.")


number_of_pieces = int(input())
pieces = {}

for _ in range(number_of_pieces):
    piece, composer, key = input().split('|')
    pieces[piece] = [composer, key]

while True:
    command = input().split('|')

    if command[0] == 'Add':
        piece, composer, key = command[1], command[2], command[3]
        add_piece(piece, composer, key, pieces)
    elif command[0] == 'Remove':
        piece = command[1]
        remove_piece(piece, pieces)
    elif command[0] == 'ChangeKey':
        piece, new_key = command[1], command[2]
        change_key(piece, new_key, pieces)
    elif command[0] == 'Stop':
        break

for piece, composer_key in pieces.items():
    print(f"{piece} -> Composer: {composer_key[0]}, Key: {composer_key[1]}")
