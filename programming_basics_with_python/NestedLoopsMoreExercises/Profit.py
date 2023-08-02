one_leva = int(input())
two_leva = int(input())
five_leva = int(input())
price = int(input())

for n1 in range(one_leva + 1):
    for n2 in range(two_leva + 1):
        for n3 in range(five_leva + 1):

            result = n1 * 1 + n2 * 2 + n3 * 5

            if result == price:
                print(f"{n1} * 1 lv. + {n2} * 2 lv. + {n3} * 5 lv. = {price} lv.")