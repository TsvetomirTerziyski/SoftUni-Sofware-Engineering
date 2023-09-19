def substring(string_one, string_two):
    while string_one in string_two:
        string_two = string_two.replace(string_one, '')
    return string_two


first_string = input()
second_string = input()

result = substring(first_string, second_string)
print(result)
