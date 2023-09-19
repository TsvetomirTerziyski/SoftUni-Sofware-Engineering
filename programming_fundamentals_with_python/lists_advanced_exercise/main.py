list_data = input().split(" ")
command = input()

while command != "3:1":
    action = command.split(" ")

    if action[0] == "merge":
        start_index = int(action[1])
        end_index = int(action[2])
        # checking if the indexes are valid with the function above
        if start_index < 0:
            start_index = 0
        if end_index > len(list_data) - 1:
            end_index = len(list_data) - 1
        # creating new word from the words in list_data index range
        new_word = ""
        for i in range(start_index, end_index + 1):
            new_word += list_data[i]
        # deleting the range from the main list and inserting the new word on its place
        del list_data[start_index:end_index + 1]
        list_data.insert(start_index, new_word)

    elif action[0] == "divide":
        index_el = int(action[1])
        partitions = int(action[2])
        # separating the word for divison from the main list while removing it from the list
        word = list_data.pop(index_el)
        divided_word = []
        # checking if partitions is more then 0 and if its less then half length of the word
        # so we know we are sure that we are going to be slicing the word
        if partitions > 0:
            # this is how many symbols per part will be sliced
            step_size = (len(word) // partitions)
            # running range that is -1 as the last part will always be done separate with whatever is left
            for _ in range(partitions - 1):
                # adding the slices to the empty
                divided_word.append(word[0:step_size])
                # slicing off the part we used already
                word = word[step_size::]
            # adding the remaining last slice to the list
            divided_word.append(word)
        # in case there is no slicing we just add the whole word to the list
        else:
            divided_word.append(word)
        # adding the list of slices back to the main list starting from the index that we are given
        for indx in range(len(divided_word)):
            list_data.insert(index_el + indx, divided_word[indx])

    command = input()

print(" ".join(list_data))