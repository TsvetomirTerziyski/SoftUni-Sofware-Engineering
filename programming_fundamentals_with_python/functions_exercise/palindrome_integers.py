def is_palindrome(lst):
    for element in lst:
        if element == element[::-1]:
            print('True')
        else:
            print('False')


input_list = input().split(', ')
is_palindrome(input_list)
