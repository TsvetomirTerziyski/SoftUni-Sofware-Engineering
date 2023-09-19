def valid_password(given_password):
    is_valid = False
    lst = []
    digit = 0
    if 6 <= len(given_password) <= 10:
        is_valid = True
        lst.append(is_valid)
    else:
        print("Password must be between 6 and 10 characters")
    if given_password.isalnum():
        is_valid = True
        lst.append(is_valid)
    else:
        print("Password must consist only of letters and digits")
    for element in given_password:
        if element.isdigit():
            digit += 1
            if digit >= 2:
                is_valid = True
                lst.append(is_valid)
                break
    else:
        print("Password must have at least 2 digits")
    if lst == [is_valid, is_valid, is_valid]:
        print("Password is valid")


password = input()
valid_password(password)
