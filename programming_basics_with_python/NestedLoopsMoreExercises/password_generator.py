n = int(input())
L = int(input())

a = ord('a')
flag = False
result = ''

for s1 in range(1,n+1):
    for s2 in range(1,n+1):
        for s3 in range(a,a+L):
            for s4 in range(a,a+L):
                for s5 in range(1,n+1):

                    result = f'{s1}{s2}{chr(s3)}{chr(s4)}{s5}'

                    if s5 > s1 and s5 > s2:
                        print(result, end=' ')


