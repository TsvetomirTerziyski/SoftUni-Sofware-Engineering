number_of_rooms = int(input())
free_chairs = 0

for current_room in range(1, number_of_rooms + 1):
     current_room_chairs_and_visitors = input().split()

     current_room_chairs = current_room_chairs_and_visitors[0]
     visitors = int(current_room_chairs_and_visitors[1])

     if len(current_room_chairs) < visitors:
          print(f"{visitors - len(current_room_chairs)} more chairs needed in room {current_room}")
          free_chairs -= visitors - len(current_room_chairs)
     else:
          free_chairs += len(current_room_chairs) - visitors

if free_chairs >= 0:
     print(f'Game On, {free_chairs} free chairs left')
