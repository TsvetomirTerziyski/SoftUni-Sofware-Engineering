n = int(input())

valid_combinations = 0

for n1 in range(n+1):
    for n2 in range(n+1):
        for n3 in range(n+1):
            if n == n1 + n2 + n3:
                valid_combinations += 1

print(valid_combinations)