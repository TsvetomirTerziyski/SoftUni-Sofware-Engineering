from math import floor


def closer_to_center_point(x1, y1, x2, y2, x3, y3, x4, y4):
    if abs(x1) + abs(y1) + abs(x2) + abs(y2) >= abs(x3) + abs(y3) + abs(x4) + abs(y4):
        if abs(x1) + abs(y1) <= abs(x2) + abs(y2):
            return f"({x1}, {y1})({x2}, {y2})"
        else:
            return f"({x2}, {y2})({x1}, {y1})"
    else:
        if abs(x3) + abs(y3) <= abs(x4) + abs(y4):
            return f"({x3}, {y3})({x4}, {y4})"
        else:
            return f"({x4}, {y4})({x3}, {y3})"


x_one = floor(float(input()))
y_one = floor(float(input()))
x_two = floor(float(input()))
y_two = floor(float(input()))
x_three = floor(float(input()))
y_three = floor(float(input()))
x_four = floor(float(input()))
y_four = floor(float(input()))
result = closer_to_center_point(x_one, y_one, x_two, y_two, x_three, y_three, x_four, y_four)
print(result)
