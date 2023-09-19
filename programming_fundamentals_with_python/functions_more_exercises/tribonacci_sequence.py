def tribonacci_sequence(num):
    sequence = [1]

    for i in range(1, num):
        if len(sequence) < 3:
            sequence.append(i)
        else:
            sequence.append(sum(sequence[-3:]))
    return sequence


n = int(input())
result = map(str, tribonacci_sequence(n))
print(' '.join(result))
