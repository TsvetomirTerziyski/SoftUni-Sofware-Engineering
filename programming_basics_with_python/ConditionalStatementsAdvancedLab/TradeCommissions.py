town = input()
sales_volume = float(input())

isValid = True
trade_commission = 0

if town == 'Sofia':
    if 0 <= sales_volume <= 500:
        trade_commission = sales_volume * 0.05
    elif 500 < sales_volume <= 1000:
        trade_commission = sales_volume * 0.07
    elif 1000 < sales_volume <= 10000:
        trade_commission = sales_volume * 0.08
    elif sales_volume > 10000:
        trade_commission = sales_volume * 0.12
    else:
        isValid = False
elif town == 'Varna':
    if 0 <= sales_volume <= 500:
        trade_commission = sales_volume * 0.045
    elif 500 < sales_volume <= 1000:
        trade_commission = sales_volume * 0.075
    elif 1000 < sales_volume <= 10000:
        trade_commission = sales_volume * 0.10
    elif sales_volume > 10000:
        trade_commission = sales_volume * 0.13
    else:
        isValid = False
elif town == 'Plovdiv':
    if 0 <= sales_volume <= 500:
        trade_commission = sales_volume * 0.055
    elif 500 < sales_volume <= 1000:
        trade_commission = sales_volume * 0.08
    elif 1000 < sales_volume <= 10000:
        trade_commission = sales_volume * 0.12
    elif sales_volume > 10000:
        trade_commission = sales_volume * 0.145
    else:
        isValid = False
else:
    isValid = False

if isValid != True:
    print('error')
else:
    print(f'{trade_commission:.2f}')
