pens_packs = int(input())
markers_packs = int(input())
preparation = int(input())
discount = int(input()) / 100

pens_price = 5.80
markers_price = 7.20
liter_preparation_price = 1.20

price_no_discount = \
    (pens_packs * pens_price) + \
    (markers_packs * markers_price) + \
    (preparation * liter_preparation_price)

total_price = price_no_discount - (price_no_discount * discount)

print(total_price)



