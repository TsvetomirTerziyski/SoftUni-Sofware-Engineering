def substring(s1, s2):
    substring_list = []
    for first_word in s1:
        for second_word in s2:
            if first_word in second_word:
                substring_list.append(first_word)
                break
    return substring_list


first_sequence = input().split(', ')
second_sequence = input().split(', ')
result = substring(first_sequence, second_sequence)
print(result)
