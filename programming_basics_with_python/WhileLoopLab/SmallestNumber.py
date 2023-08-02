import sys

min_num = sys.maxsize

while True:
    num = (input())

    if num == "Stop":
        break

    num = int(num)

    if num < min_num:
        min_num = num

print(min_num)

