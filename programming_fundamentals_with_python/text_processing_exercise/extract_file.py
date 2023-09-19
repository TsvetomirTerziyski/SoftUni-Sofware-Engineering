file_path_list = input().split('\\')

file_name, extension = file_path_list[-1].split('.')

print(f"File name: {file_name}")
print(f"File extension: {extension}")
