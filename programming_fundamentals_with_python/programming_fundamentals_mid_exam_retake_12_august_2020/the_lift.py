people_waiting_for_the_lift = int(input())
current_state_of_the_lift = [int(i) for i in input().split()]
max_seats = 4

for index in range(len(current_state_of_the_lift)):
    removed_people = 0
    if current_state_of_the_lift[index] < max_seats and people_waiting_for_the_lift >= max_seats:
        removed_people += max_seats - current_state_of_the_lift[index]
        current_state_of_the_lift[index] += max_seats - current_state_of_the_lift[index]
        people_waiting_for_the_lift -= removed_people

    elif people_waiting_for_the_lift < max_seats:
        current_state_of_the_lift[index] += people_waiting_for_the_lift
        people_waiting_for_the_lift -= people_waiting_for_the_lift

if people_waiting_for_the_lift == 0 and current_state_of_the_lift[-1] < 4:
    print("The lift has empty spots!")
    print(' '.join([str(i) for i in current_state_of_the_lift]))
elif people_waiting_for_the_lift > 0 and current_state_of_the_lift[-1] == 4:
    print(f"There isn't enough space! {people_waiting_for_the_lift} people in a queue!")
    print(' '.join([str(i) for i in current_state_of_the_lift]))
else:
    print(' '.join([str(i) for i in current_state_of_the_lift]))
