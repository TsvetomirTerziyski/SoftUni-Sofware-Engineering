n = int(input())
word = input()
lst = []
list_with_the_word_included = []

for _ in range(n):
    current_string = input()

    lst.append(current_string)

    if word in current_string:
        list_with_the_word_included.append(current_string)

print(lst)
print(list_with_the_word_included)
