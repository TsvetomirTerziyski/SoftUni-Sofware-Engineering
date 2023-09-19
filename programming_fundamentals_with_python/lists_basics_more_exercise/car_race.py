input_list = input().split(' ')
left_car_sum = 0
right_car_sum = 0
left_car_int_list = []
right_car_int_list = []
winner = ''

finish_line = len(input_list) // 2
left_car = input_list[:finish_line]
right_car = input_list[-1:finish_line:-1]

for index in range(len(left_car)):
    left_car_int_list.append(int(left_car[index]))
    left_car_sum += left_car_int_list[index]

    right_car_int_list.append(int(right_car[index]))
    right_car_sum += right_car_int_list[index]

    if left_car_int_list[index] == 0:
        left_car_sum -= left_car_sum * 0.2
    elif right_car_int_list[index] == 0:
        right_car_sum -= right_car_sum * 0.2

if left_car_sum < right_car_sum:
    winner = 'left'
    print(f"The winner is {winner} with total time: {left_car_sum:.1f}")
else:
    winner = 'right'
    print(f"The winner is {winner} with total time: {right_car_sum:.1f}")
