collect_resources_dict = {}
while True:
    resource = input()

    if resource == 'stop':
        break

    quantity = int(input())

    if resource not in collect_resources_dict:
        collect_resources_dict[resource] = 0
    collect_resources_dict[resource] += quantity

for resource, quantity in collect_resources_dict.items():
    print(f'{resource} -> {quantity}')
