def char_multiplier(string_one, string_two):
    total_sum = 0

    if len(string_one) > len(string_two):
        for index in range(len(string_two)):
            total_sum += ord(string_one[index]) * ord(string_two[index])
        for index in range(len(string_two), len(string_one)):
            total_sum += ord(string_one[index])
    elif len(string_one) < len(string_two):
        for index in range(len(string_one)):
            total_sum += ord(string_one[index]) * ord(string_two[index])
        for index in range(len(string_one), len(string_two)):
            total_sum += ord(string_two[index])
    else:
        for index in range(len(string_one)):
            total_sum += ord(string_one[index]) * ord(string_two[index])

    return total_sum


first_string, second_string = input().split()

print(char_multiplier(first_string, second_string))
