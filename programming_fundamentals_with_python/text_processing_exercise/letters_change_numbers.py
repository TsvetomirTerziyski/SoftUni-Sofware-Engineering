def total_sum_from_the_game(list):
    total_sum = 0
    current_sum = 0
    for text in list:
        first_letter, last_letter = text[0], text[-1]
        number = int(text[1:len(text) - 1])
        current_sum = number
        if first_letter.isupper():
            current_sum /= ord(first_letter) - 64
        elif first_letter.islower():
            current_sum *= ord(first_letter) - 96
        if last_letter.isupper():
            current_sum -= ord(last_letter) - 64
        elif last_letter.islower():
            current_sum += ord(last_letter) - 96
        total_sum += current_sum
    return total_sum


input_list = [element.strip() for element in input().split()]
print(f'{total_sum_from_the_game(input_list):.2f}')
