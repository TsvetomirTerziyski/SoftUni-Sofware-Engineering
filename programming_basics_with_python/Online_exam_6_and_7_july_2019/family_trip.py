budget = float(input())
nights = int(input())
price_for_day = float(input())
percent_for_additional_expenses = int(input()) * 0.01

if nights > 7:
    price_for_day *= 0.95
    price_all_days = nights * price_for_day
    expenses = percent_for_additional_expenses * budget
    total_price = price_all_days + expenses
else:
    price_all_days = nights * price_for_day
    expenses = percent_for_additional_expenses * budget
    total_price = price_all_days + expenses

if total_price <= budget:
    print(f"Ivanovi will be left with {budget - total_price:.2f} leva after vacation.")
else:
    print(f"{total_price - budget:.2f} leva needed.")