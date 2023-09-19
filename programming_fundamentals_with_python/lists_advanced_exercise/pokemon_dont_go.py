input_list = [int(x) for x in input().split()]
removed_elements = []

while len(input_list) > 0:
    index = int(input())
    if index in range(len(input_list)):
        removed_element = input_list.pop(index)
        removed_elements.append(removed_element)
        for index in range(len(input_list)):
            if input_list[index] <= removed_element:
                input_list[index] += removed_element
            elif input_list[index] > removed_element:
                input_list[index] -= removed_element

    elif index < 0:
        removed_element = input_list.pop(0)
        removed_elements.append(removed_element)
        input_list.insert(0, input_list[-1])
        for element in input_list:
            element_index = input_list.index(element)
            if element <= removed_element:
                input_list[element_index] += removed_element
            elif element > removed_element:
                input_list[element_index] -= removed_element

    elif index > len(input_list) - 1:
        removed_element = input_list.pop(-1)
        removed_elements.append(removed_element)
        input_list.insert(len(input_list), input_list[0])
        for element in input_list:
            element_index = input_list.index(element)
            if element <= removed_element:
                input_list[element_index] += removed_element
            elif element > removed_element:
                input_list[element_index] -= removed_element

summed_value = sum(removed_elements)
print(summed_value)
