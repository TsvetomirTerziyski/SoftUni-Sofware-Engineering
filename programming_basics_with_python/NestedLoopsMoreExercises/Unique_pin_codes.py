max_n1 = int(input())
max_n2 = int(input())
max_n3 = int(input())

for n1 in range(2, max_n1+1, 2):
    for n2 in range(2, max_n2+1):
        for n3 in range(2, max_n3+1,2):

         if n2 == 2 or n2 == 3 or n2 == 5 or n2 == 7:

             print(n1,end=' ')
             print(n2,end=' ')
             print(n3)
