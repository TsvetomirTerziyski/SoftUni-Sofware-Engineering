def sum_numbers(num_one, num_two):
    return num_one + num_two

def subtract(result, num_three):
    return result - num_three

def add_and_subtract(n1, n2, n3):
    sum_of_first_two = sum_numbers(first_number, second_number)
    result_minus_third = subtract(sum_of_first_two, third_number)
    return result_minus_third


first_number = int(input())
second_number = int(input())
third_number = int(input())

print(add_and_subtract(first_number, second_number, third_number))
