def repeat_string(list_of_strings):
    final_string = ''
    for string in list_of_strings:
        final_string += string * len(string)
    return final_string


strings_list = input().split()

result = repeat_string(strings_list)
print(result)
