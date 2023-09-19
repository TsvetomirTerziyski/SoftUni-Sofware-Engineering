courses = {}

while True:
    command = input().split(' : ')

    if command[0] == 'end':
        break

    course, name = command[0], command[1]

    if course not in courses:
        courses[course] = []
    courses[course].append(name)

for course, names in courses.items():
    print(f'{course}: {len(courses[course])}')
    for name in names:
        print(f"-- {name}")
