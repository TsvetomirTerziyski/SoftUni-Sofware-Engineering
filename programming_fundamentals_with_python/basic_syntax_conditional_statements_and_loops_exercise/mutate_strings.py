string_one = input()
string_two = input()

for index in range(len(string_two)):

    final_string = string_two[:index+1] + string_one[index+1:]
    if string_two[index] == string_one[index]:
        continue
    else:
        print(final_string)
