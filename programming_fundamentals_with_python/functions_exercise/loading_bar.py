def loading_bar(num):
    percent_signs = num // 10
    percent_sign = '%' * percent_signs
    dots_count = 10 - percent_signs
    dots = '.' * dots_count

    if num == 100:
        print(f'{num}% Complete!')
        print('[%%%%%%%%%%]')
    else:
        print(f'{num}% [{percent_sign}{dots}]')
        print("Still loading...")


number = int(input())
loading_bar(number)
