results = {}
submissions = {}

while True:
    command = input()

    if command == "exam finished":
        break

    command = command.split('-')
    if len(command) == 3:
        username, language, points = command[0], command[1], int(command[2])
        if username not in results.keys():
            results[username] = points
        elif username in results.keys():
            if results[username] < points:
                results[username] = points

        if language not in submissions.keys():
            submissions[language] = 0
        submissions[language] += 1

    elif len(command) == 2:
        name, banned = command[0], command[1]
        del results[name]

print('Results:')
for username, points in results.items():
    print(f'{username} | {points}')
print('Submissions:')
for language, submission in submissions.items():
    print(f'{language} - {submission}')
