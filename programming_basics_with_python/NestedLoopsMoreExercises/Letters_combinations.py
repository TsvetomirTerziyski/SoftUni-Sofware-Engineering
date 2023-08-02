first_letter = ord(input())
last_letter = ord(input())
letter_to_miss = ord(input())

valid_combinations = 0

for n1 in range(first_letter, last_letter + 1):
    for n2 in range(first_letter, last_letter + 1):
        for n3 in range(first_letter, last_letter + 1):
            if n1 == letter_to_miss or n2 == letter_to_miss or n3 == letter_to_miss:
                continue
            else:
                valid_combinations += 1

            print(f"{chr(n1)}{chr(n2)}{chr(n3)}", end=" ")
print(valid_combinations)


