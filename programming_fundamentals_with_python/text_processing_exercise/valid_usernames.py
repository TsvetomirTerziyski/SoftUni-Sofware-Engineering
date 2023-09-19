def valid_length(username):
    if 3 <= len(username) <= 16:
        return True
    return False


def valid_symbols(username):
    if not (username.isalnum() or '-' in username or '_' in username):
        return False
    return True


def no_redundant_symbols(username):
    if ' ' in username:
        return False
    return True


def valid_username(username):
    if valid_length(username) and valid_symbols(username) and no_redundant_symbols(username):
        return True
    return False


usernames_list = input().split(', ')

for username in usernames_list:
    if valid_username(username):
        print(username)
