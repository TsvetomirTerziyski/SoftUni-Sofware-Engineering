len_centimeters = int(input())
width_centimeters = int(input())
height_centimeters = int(input())
percent = float(input())

volume = len_centimeters * width_centimeters * height_centimeters
volume_liters = volume / 1000
liters_aquarium = volume_liters - ((percent / 100) * volume_liters)

print(liters_aquarium)