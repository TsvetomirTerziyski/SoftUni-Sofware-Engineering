dictionary = {}

command = input().split(' -> ')

while command[0] != 'End':
    company_name, emp_id = command[0], command[1]

    if company_name not in dictionary:
        dictionary[company_name] = []

    if emp_id not in dictionary[company_name]:
        dictionary[company_name].append(emp_id)

    command = input().split(' -> ')

for company, emp in dictionary.items():
    print(company)
    for employee in emp:
        print(f'-- {employee}')
