grade = float(input())


def grade_result_word(n):
    if 2 <= n <= 2.99:
        return 'Fail'
    elif 3.00 <= n <= 3.49:
        return 'Poor'
    elif 3.50 <= n <= 4.49:
        return 'Good'
    elif 4.50 <= n <= 5.49:
        return 'Very Good'
    elif 5.50 <= n <= 6.00:
        return 'Excellent'


print(grade_result_word(grade))
