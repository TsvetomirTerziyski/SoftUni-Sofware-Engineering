def happy_employees(lst):
    improved_happiness_list = list(map(lambda x: x * happiness_improvement_factor, lst))
    average_happiness = sum(improved_happiness_list) / len(improved_happiness_list)
    total_count = len(improved_happiness_list)
    happy_count = list(filter(lambda x: x >= average_happiness, improved_happiness_list))

    if len(happy_count) >= total_count / 2:
        return f"Score: {len(happy_count)}/{total_count}. Employees are happy!"
    else:
        return f"Score: {len(happy_count)}/{total_count}. Employees are not happy!"


emp_happiness_list = map(int,input().split())
happiness_improvement_factor = int(input())
result = happy_employees(emp_happiness_list)
print(result)
