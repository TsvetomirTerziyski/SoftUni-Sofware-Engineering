inp = input()
lst = inp.split(", ")

if lst[len(lst)-1] == 'wolf':
    print("Please go away and stop eating my sheep")

for index in range(len(lst)):
    if lst[index] == 'wolf' and lst[len(lst)-1] != 'wolf':
        print(f"Oi! Sheep number {len(lst)-(index+1)}! You are about to be eaten by a wolf!")
        break
