number_chicken_menu = int(input())
number_fish_menu = int(input())
number_vegetarian_menu = int(input())

chicken_menu_price = 10.35
fish_menu_price = 12.40
vegetarian_menu_price = 8.15
delivery_price = 2.50

total_bill_excluding_delivery = number_chicken_menu * chicken_menu_price + \
    number_fish_menu * fish_menu_price + \
    number_vegetarian_menu * vegetarian_menu_price

desert_price = total_bill_excluding_delivery * 0.20

total_bill = total_bill_excluding_delivery + desert_price + delivery_price

print(total_bill)