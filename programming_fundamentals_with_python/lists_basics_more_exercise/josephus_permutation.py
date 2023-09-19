input_list = input().split(' ')
k = int(input())
final_list = []
counter = 0
index = 0

while len(input_list) > 0:
    counter += 1

    if counter % k == 0:
        final_list.append(int(input_list.pop(index)))
    else:
        index += 1

    if index >= len(input_list):
        index = 0

print(str(final_list).replace(' ', ''))
