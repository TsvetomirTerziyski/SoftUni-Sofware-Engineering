import re

count_of_barcodes = int(input())
pattern = r'(@#+)([A-Z]{1}[A-Za-z0-9]{4,}[A-Z]{1})(@#+)'
match_groups = []

for _ in range(count_of_barcodes):
    current_barcode = input()

    match = re.findall(pattern, current_barcode)

    if match:
        for element in match[0][1]:
            if element.isdigit():
                match_groups.append(element)
        if len(match_groups) == 0:
            print(f"Product group: 00")
        else:
            print(f"Product group: {''.join(match_groups)}")
            match_groups = []
    else:
        print(f"Invalid barcode")
