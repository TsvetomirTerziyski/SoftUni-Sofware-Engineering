def even_odd_sum(number):
    even_sum = 0
    odd_sum = 0

    for num in number:
        if int(num) % 2 == 0:
            even_sum += int(num)
        else:
            odd_sum += int(num)
    return even_sum, odd_sum


input_number = input()
even_sum, odd_sum = even_odd_sum(input_number)
result = f"Odd sum = {odd_sum}, Even sum = {even_sum}"
print(result)
