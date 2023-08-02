first_pair_beginning = int(input())
second_pair_beginning = int(input())
first_pair_difference = int(input())
second_pair_difference = int(input())

for n1 in range(first_pair_beginning,(first_pair_beginning + first_pair_difference)+1):
    for n2 in range(second_pair_beginning,(second_pair_beginning+second_pair_difference)+1):

        if (n1 % 2 != 0 and n1 % 3 != 0 and n1 % 5 != 0 and n1 % 7 != 0) and (n2 % 2 != 0 and n2 % 3 != 0 and n2 % 5 != 0 and n2 % 7 != 0):

            print(f'{n1}{n2}')
