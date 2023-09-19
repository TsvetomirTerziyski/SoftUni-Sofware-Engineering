input_text = input()

lowered = input_text.lower()
result = lowered.count('sand') + lowered.count('water') + lowered.count('fish') + lowered.count('sun')

print(result)
