number = int(input())

lst = [n for n in str(number)]
lst.sort(reverse=True)

join = ''.join(lst)
print(int(join))
