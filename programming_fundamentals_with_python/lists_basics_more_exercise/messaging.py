input_list = input().split(' ')
input_string = input()
message = []
new_string = input_string

for sequence in input_list:
    sum_sequence = 0
    for number in sequence:
        sum_sequence += int(number)
    sum_sequence %= len(input_string)
    message.append(input_string[sum_sequence])
    new_string = input_string.replace(input_string[sum_sequence], '', 1)
    input_string = new_string

print(('').join(message))
