number_of_pages = int(input())
pages_for_hour = int(input())
days = int(input())

time_for_whole_book = number_of_pages / pages_for_hour
hours_a_day = time_for_whole_book // days

print(hours_a_day)