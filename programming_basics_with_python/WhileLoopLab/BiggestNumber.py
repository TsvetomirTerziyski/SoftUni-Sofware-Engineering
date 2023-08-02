import sys

max_num = -sys.maxsize

while True:
    num = (input())

    if num == "Stop":
        break

    num = int(num)

    if num > max_num:
        max_num = num

print(max_num)

