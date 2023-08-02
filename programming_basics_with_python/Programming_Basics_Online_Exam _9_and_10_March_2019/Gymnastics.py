country = input()
tool = input()

total_result = 0
percent = 0
points_needed_for_max_score = 0

if country == 'Bulgaria' and tool == 'ribbon':
    total_result = 9.600 + 9.400
    points_needed_for_max_score = 20 - total_result
    percent = (points_needed_for_max_score / 20) * 100
elif country == 'Russia' and tool == 'ribbon':
    total_result = 9.100 + 9.400
    points_needed_for_max_score = 20 - total_result
    percent = (points_needed_for_max_score / 20) * 100
elif country == 'Italy' and tool == 'ribbon':
    total_result = 9.200 + 9.500
    points_needed_for_max_score = 20 - total_result
    percent = (points_needed_for_max_score / 20) * 100

if country == 'Bulgaria' and tool == 'hoop':
    total_result = 9.550 + 9.750
    points_needed_for_max_score = 20 - total_result
    percent = (points_needed_for_max_score / 20) * 100
elif country == 'Russia' and tool == 'hoop':
    total_result = 9.300 + 9.800
    points_needed_for_max_score = 20 - total_result
    percent = (points_needed_for_max_score / 20) * 100
elif country == 'Italy' and tool == 'hoop':
    total_result = 9.450 + 9.350
    points_needed_for_max_score = 20 - total_result
    percent = (points_needed_for_max_score / 20) * 100

if country == 'Bulgaria' and tool == 'rope':
    total_result = 9.500 + 9.400
    points_needed_for_max_score = 20 - total_result
    percent = (points_needed_for_max_score / 20) * 100
elif country == 'Russia' and tool == 'rope':
    total_result = 9.600 + 9.000
    points_needed_for_max_score = 20 - total_result
    percent = (points_needed_for_max_score / 20) * 100
elif country == 'Italy' and tool == 'rope':
    total_result = 9.700 + 9.150
    points_needed_for_max_score = 20 - total_result
    percent = (points_needed_for_max_score / 20) * 100

print(f"The team of {country} get {total_result:.3f} on {tool}.")
print(f"{percent:.2f}%")