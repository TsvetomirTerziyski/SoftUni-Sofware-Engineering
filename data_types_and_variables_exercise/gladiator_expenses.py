lost_fights = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

broken_helmets = lost_fights // 2
broken_swords = lost_fights // 3
broken_shields = lost_fights // (2*3)
broken_armors = lost_fights // 12

total_price = (helmet_price * broken_helmets) + (sword_price * broken_swords) \
              + (shield_price * broken_shields) + (armor_price * broken_armors)

print(f"Gladiator expenses: {total_price:.2f} aureus")
