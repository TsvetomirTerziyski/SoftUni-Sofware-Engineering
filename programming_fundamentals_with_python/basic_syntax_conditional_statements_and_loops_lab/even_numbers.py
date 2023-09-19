received_number = int(input())

for n in range(received_number):
    number = int(input())

    if number % 2 == 1:
        print(f"{number} is odd!" )
        break
else:
    print("All numbers are even.")