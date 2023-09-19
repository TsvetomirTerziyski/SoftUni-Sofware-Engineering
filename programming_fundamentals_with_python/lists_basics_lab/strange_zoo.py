lst = []

tail = lst.append(input())
body = lst.append(input())
head = lst.append(input())

lst[0], lst[2] = lst[2], lst[0]

print(lst)
