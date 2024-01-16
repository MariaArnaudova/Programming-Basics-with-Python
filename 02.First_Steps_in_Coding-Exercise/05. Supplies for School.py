chemicals_count = int(input())
markers_count = int(input())
detergent_count = int(input())

chemicals_price = 5.80
markers_price = 7.20
detergent_price = 1.20

all_materials_price = chemicals_count * chemicals_price + \
    markers_count * markers_price + \
    detergent_count * detergent_price

discount = 0.25

price_with_discount = all_materials_price * (1 - discount)

print(price_with_discount)