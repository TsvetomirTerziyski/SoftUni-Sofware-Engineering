def positive_numbers(list_of_numbers):
    positive_list = [num for num in list_of_numbers if num >= 0]
    return positive_list


def negative_numbers(list_of_numbers):
    negative_list = [num for num in list_of_numbers if num < 0]
    return negative_list


def even_numbers(list_of_numbers):
    even_list = [num for num in list_of_numbers if num % 2 == 0]
    return even_list


def odd_numbers(list_of_numbers):
    odd_list = [num for num in list_of_numbers if num % 2 != 0]
    return odd_list


numbers_list = [int(num) for num in input().split(', ')]
positive = ', '.join([str(num) for num in positive_numbers(numbers_list)])
negative = ', '.join([str(num) for num in negative_numbers(numbers_list)])
even = ', '.join([str(num) for num in even_numbers(numbers_list)])
odd = ', '.join([str(num) for num in odd_numbers(numbers_list)])

print(f'Positive: {positive}')
print(f'Negative: {negative}')
print(f'Even: {even}')
print(f'Odd: {odd}')
