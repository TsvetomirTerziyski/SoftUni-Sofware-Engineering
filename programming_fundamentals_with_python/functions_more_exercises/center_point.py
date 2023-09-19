from math import floor


def closer_to_center_point(x1, y1, x2, y2):
    if abs(x1) + abs(y1) < abs(x2) + abs(y2):
        return f"({x1}, {y1})"
    elif abs(x1) + abs(y1) > abs(x2) + abs(y2):
        return f"({x2}, {y2})"
    else:
        return f"({x1}, {y1})"



x_one = floor(float(input()))
y_one = floor(float(input()))
x_two = floor(float(input()))
y_two = floor(float(input()))
first_coordinates_list = [x_one, y_one]
second_coordinates_list = [x_two, y_two]
result = closer_to_center_point(x_one, y_one, x_two, y_two)
print(result)
