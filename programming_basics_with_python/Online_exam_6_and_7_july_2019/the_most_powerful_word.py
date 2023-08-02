from math import floor
best_word = ''
best_Score = 0
first_digit = ''
while True:
    command = input()

    if command == 'End of words':
        break

    word = command
    current_sum = 0
    current_score = 0

    for index, digit in enumerate(word):
        current_sum += ord(digit)

        if index == 0:
            first_digit = digit

        if first_digit == 'a' or first_digit == 'e' or first_digit == 'i' or first_digit == 'o' or first_digit == 'u' or first_digit == 'y' or first_digit == 'A' or first_digit == 'E' or first_digit == 'I' or first_digit == 'O' or first_digit == 'U' or first_digit == 'Y':
            current_score = current_sum * len(word)
        else:
            current_score = floor(current_sum / len(word))

        if current_score > best_Score:
            best_Score = current_score
            best_word = word

print(f"The most powerful word is {best_word} - {best_Score}" )
