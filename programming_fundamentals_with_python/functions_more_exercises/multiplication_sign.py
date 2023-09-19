def multiplication_result(lst):
    counter = 0
    if 0 in lst:
        return 'zero'

    for element in lst:
        if element < 0:
            counter += 1
    if counter % 2 == 0:
        return 'positive'
    else:
        return 'negative'


number_one = int(input())
number_two = int(input())
number_three = int(input())
list_from_numbers = [number_one, number_two, number_three]
result = multiplication_result(list_from_numbers)
print(result)
