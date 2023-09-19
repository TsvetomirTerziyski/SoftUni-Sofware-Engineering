year = int(input())

while True:
    year += 1

    if len(set(str(year))) == len(list(str(year))):
        break

print(year)
