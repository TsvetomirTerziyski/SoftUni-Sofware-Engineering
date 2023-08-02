control_minutes = int(input())
control_seconds = int(input())
length_in_meters = float(input())
seconds_for_hundred_meters = int(input())

control_in_seconds = control_minutes * 60 + control_seconds
times_time_decrease = length_in_meters / 120
total_time_decrease = times_time_decrease * 2.5
Marin_time = (length_in_meters / 100) * seconds_for_hundred_meters - total_time_decrease

if Marin_time <= control_in_seconds:
    print("Marin Bangiev won an Olympic quota!")
    print(f"His time is {Marin_time:.3f}.")
else:
    print(f"No, Marin failed! He was {abs(control_in_seconds - Marin_time):.3f} second slower.")
