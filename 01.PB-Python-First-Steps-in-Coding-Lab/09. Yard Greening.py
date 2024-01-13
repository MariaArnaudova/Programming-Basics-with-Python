gardenArea = float(input())
price = 7.61
discount = 0.18

gardenPrice = gardenArea * price
priceWithDiscount = gardenPrice * discount

finalPrice = gardenPrice - priceWithDiscount
print(f'The final price is: {finalPrice} lv.')
print(f'The discount is: {priceWithDiscount} lv.')