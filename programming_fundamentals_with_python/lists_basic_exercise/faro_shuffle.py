deck = input().split()
count_of_shuffles = int(input())

middle_of_deck = len(deck) // 2

for _ in range(count_of_shuffles):
    lst_after_shuffle = []
    left_part = deck[:middle_of_deck]
    right_part = deck[middle_of_deck:]
    for index in range(len(left_part)):
        lst_after_shuffle.append(left_part[index])
        lst_after_shuffle.append(right_part[index])
    deck = lst_after_shuffle

print(deck)
