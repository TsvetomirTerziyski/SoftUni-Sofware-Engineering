def palindrome_count(lst):
    palindrome_lst = [word for word in lst if word == word[::-1]]
    palindrome_counter = palindrome_lst.count(palindrome)

    print(palindrome_lst)
    print(f"Found palindrome {palindrome_counter} times")


input_list = input().split()
palindrome = input()
palindrome_count(input_list)
