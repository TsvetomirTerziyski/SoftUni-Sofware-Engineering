number_of_electrons = int(input())
shells = []
shell_counter = 1

while number_of_electrons > 0:
    if number_of_electrons < 2 * (shell_counter ** 2):
        shells.append(number_of_electrons)
    else:
        shells.append((2 * (shell_counter ** 2)))

    number_of_electrons -= 2 * (shell_counter ** 2)
    shell_counter += 1

print(shells)
