from math import ceil

movie_name = input()
episode_length = int(input())
rest_length = int(input())

lunch_time = rest_length / 8
leisure_time = rest_length / 4
total_rest = lunch_time + leisure_time + episode_length
time_left = rest_length - total_rest

if time_left >= 0:
    print(f'You have enough time to watch {movie_name} and left with {ceil(time_left)} minutes free time.')
else:
    print(f"You don't have enough time to watch {movie_name}, you need {ceil(abs(time_left))} more minutes.")
