exam_hour = int(input())
exam_minute = int(input())
arrival_hour = int(input())
arrival_minute = int(input())

exam_start_in_minutes = exam_hour * 60 + exam_minute
arrival_in_minutes = arrival_hour * 60 + arrival_minute

time_diff = arrival_in_minutes - exam_start_in_minutes


if -30 <= time_diff < 0:
    print('On time')
    print(f'{abs(time_diff)} minutes before the start')
elif time_diff == 0:
    print('On time')
elif -60 < time_diff < 0:
    print('Early')
    print(f'{abs(time_diff)} minutes before the start')
elif time_diff <= -60:
    hours = abs(time_diff) // 60
    minutes = abs(time_diff) % 60
    print('Early')
    print(f'{hours} : {minutes:02d} hours before the start')
elif 0 < time_diff < 60:
    print('Late')
    print(f'{time_diff} minutes after the start')
elif time_diff >= 60:
    hours = time_diff // 60
    minutes = time_diff % 60
    print('Late')
    print(f'{hours} : {minutes:02d} hours after the start')


