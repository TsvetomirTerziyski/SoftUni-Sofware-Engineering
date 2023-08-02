budget = float(input())

videocards = int(input())
processors = int(input())
ram_memories = int(input())

videocard_price = 250

videocards_price = videocard_price * videocards
processors_price = processors * (videocards_price * 0.35)
ram_memories_price = ram_memories * (videocards_price * 0.10)

total_price = videocards_price + processors_price + ram_memories_price

if videocards > processors:
    total_price *= 0.85

if total_price <= budget:
    print(f'You have {budget - total_price:.2f} leva left!')
else:
    print(f'Not enough money! You need {total_price - budget:.2f} leva more!')
