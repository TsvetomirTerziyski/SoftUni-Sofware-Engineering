wall_height = int(input())
wall_width = int(input())
percent_not_to_paint = int(input()) / 100

volume = wall_height * wall_width * 4
walls_to_paint = volume - (percent_not_to_paint*volume)


while True:
    command = input()

    if command == 'Tired!':
        print(f"{int(walls_to_paint)} quadratic m left." )
        break

    paint_l = int(command)

    walls_to_paint -= paint_l

    if walls_to_paint < 0:
        print(f"All walls are painted and you have {int(abs(walls_to_paint))} l paint left!")
        break
    if walls_to_paint == 0:
        print("All walls are painted! Great job, Pesho!")
        break