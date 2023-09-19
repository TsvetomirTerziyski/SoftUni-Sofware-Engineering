text = input().upper()
current_string = ''
final_string = ''
repetitions = ''

for index in range(len(text)):
    if not text[index].isdigit():
        current_string += text[index]
    elif text[index].isdigit():
        for digit_index in range(index, len(text)):
            if text[digit_index].isdigit():
                repetitions += text[digit_index]
            else:
                break
        final_string += current_string * int(repetitions)
        current_string = ''
        repetitions = ''

print(f"Unique symbols used: {len(set(final_string))}")
print(final_string)
