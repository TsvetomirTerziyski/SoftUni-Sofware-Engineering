current_version = input().split('.')
string_current = ''.join(current_version)
int_current = int(string_current)
current_version_plus_one = int_current + 1
current_plus_one_string = str(current_version_plus_one)
list_result = [x for x in current_plus_one_string]
result = '.'.join(list_result)
print(result)
