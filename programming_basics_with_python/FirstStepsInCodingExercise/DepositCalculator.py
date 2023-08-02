deposit_sum = float(input())
deposit_term = int(input())
annual_interest_rate = float(input()) / 100

total_sum = deposit_sum + deposit_term * ((deposit_sum * annual_interest_rate) / 12)

print(total_sum)