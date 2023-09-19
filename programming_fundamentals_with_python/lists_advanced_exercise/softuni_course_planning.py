def add_lesson(titles_list, title_of_the_lesson):
    if title_of_the_lesson not in titles_list:
        titles_list.append(title_of_the_lesson)
    return titles_list


def insert_lesson(titles_list, title_of_the_lesson, insert_index):
    if title_of_the_lesson not in titles_list:
        titles_list.insert(insert_index, title_of_the_lesson)
    return titles_list


def remove_lesson(titles_list, title_of_the_lesson):
    if title_of_the_lesson in titles_list:
        title_of_the_lesson_index = titles_list.index(title_of_the_lesson)
        if title_of_the_lesson_index + 1 in range(len(titles_list)):
            if 'Exercise' in titles_list[title_of_the_lesson_index + 1]:
                titles_list.pop(title_of_the_lesson_index + 1)
        titles_list.remove(title_of_the_lesson)
    return titles_list


def swap_lessons(titles_list, title_of_the_lesson, title_of_the_other_lesson):
    if title_of_the_lesson in titles_list and title_of_the_other_lesson in titles_list:
        title_of_the_lesson_index = titles_list.index(title_of_the_lesson)
        title_of_the_other_lesson_index = titles_list.index(title_of_the_other_lesson)

        title_of_the_lesson_has_exercise = False
        title_of_the_other_lesson_has_exercise = False

        if title_of_the_lesson_index + 1 in range(len(titles_list)):
            if 'Exercise' in titles_list[title_of_the_lesson_index + 1]:
                title_of_the_lesson_has_exercise = True
        if title_of_the_other_lesson_index + 1 in range(len(titles_list)):
            if 'Exercise' in titles_list[title_of_the_other_lesson_index + 1]:
                title_of_the_other_lesson_has_exercise = True
        titles_list[title_of_the_lesson_index], titles_list[title_of_the_other_lesson_index] = \
        titles_list[title_of_the_other_lesson_index], titles_list[title_of_the_lesson_index]

        if title_of_the_lesson_has_exercise and title_of_the_other_lesson_has_exercise:
            titles_list[title_of_the_lesson_index + 1], titles_list[title_of_the_other_lesson_index + 1] = \
            titles_list[title_of_the_other_lesson_index + 1], titles_list[title_of_the_lesson_index + 1]
        elif not title_of_the_lesson_has_exercise and title_of_the_other_lesson_has_exercise:
            titles_list.insert(title_of_the_lesson_index + 1, titles_list.pop(title_of_the_other_lesson_index + 1))
        elif title_of_the_lesson_has_exercise and not title_of_the_other_lesson_has_exercise:
            titles_list.insert(title_of_the_other_lesson_index + 1, titles_list.pop(title_of_the_lesson_index + 1))
    return titles_list


def exercise(titles_list, title_of_the_lesson):
    if title_of_the_lesson in titles_list and not f'{title_of_the_lesson}-Exercise' in titles_list:
        title_of_the_lesson_index = titles_list.index(title_of_the_lesson)
        titles_list.insert(title_of_the_lesson_index + 1, f"{title_of_the_lesson}-Exercise")
    elif title_of_the_lesson not in titles_list and not f'{title_of_the_lesson}-Exercise' in titles_list :
        titles_list.append(title_of_the_lesson)
        titles_list.append(f'{title_of_the_lesson}-Exercise')
    return titles_list


schedule_list = input().split(', ')
command = input()

while command != 'course start':
    command = command.split(':')

    activity, lesson_title = command[0], command[1]
    if 'Add' in command:
        schedule_list = add_lesson(schedule_list, lesson_title)
    elif 'Insert' in command:
        index = int(command[2])
        schedule_list = insert_lesson(schedule_list, lesson_title, index)
    elif 'Remove' in command:
        schedule_list = remove_lesson(schedule_list, lesson_title)
    elif 'Swap' in command:
        other_lesson_title = command[2]
        schedule_list = swap_lessons(schedule_list, lesson_title, other_lesson_title)
    elif 'Exercise' in command:
        schedule_list = exercise(schedule_list, lesson_title)

    command = input()

for index, element in enumerate(schedule_list):
    print(f'{index + 1}.{element}')
