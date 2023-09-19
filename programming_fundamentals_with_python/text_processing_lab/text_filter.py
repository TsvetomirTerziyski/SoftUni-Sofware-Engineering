def banned_words_replacement(list_of_banned_words, string):
    for word in list_of_banned_words:
        string = string.replace(word, '*' * len(word))
    return string


banned_list = input().split(', ')
text = input()

print(banned_words_replacement(banned_list, text))
