desired_height = int(input())

beginning_height = desired_height - 30
unsuccessful_jump = 0
successful_jump = 0
total_jumps = 0

while True:
    current_jump = int(input())
    total_jumps += 1

    if current_jump > beginning_height:
        successful_jump += 1
        beginning_height += 5
        unsuccessful_jump = 0
    else:
        unsuccessful_jump += 1

    if unsuccessful_jump == 3:
        print(f"Tihomir failed at {beginning_height}cm after {total_jumps} jumps.")
        break

    if beginning_height > desired_height:
        print(f"Tihomir succeeded, he jumped over {desired_height}cm after {total_jumps} jumps.")
        break

