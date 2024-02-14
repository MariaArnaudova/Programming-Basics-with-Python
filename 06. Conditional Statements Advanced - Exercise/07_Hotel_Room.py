month = input()
number_of_overnight = int(input())

apartment_price = 0.0
studio_price = 0.0
discount = 0.0
price_entire_stay = 0.0

if month == 'May' or month == 'October':
    studio_price = 50
    apartment_price = 65
elif month == 'June' or month == 'September':
    studio_price = 75.20
    apartment_price = 68.70
elif month == 'July' or month == 'August':
    studio_price = 76
    apartment_price = 77

price_entire_stay_studio = number_of_overnight * studio_price
price_entire_stay_apartment = number_of_overnight * apartment_price

if (month == 'May' or month == 'October') and number_of_overnight > 14:
    discount = 0.30
    price_entire_stay_studio =  price_entire_stay_studio * (1 - discount)
elif (month == 'May' or month == 'October') and number_of_overnight > 7:
    discount = 0.05
    price_entire_stay_studio = price_entire_stay_studio * (1 - discount)
elif (month == 'June' or month == 'September') and number_of_overnight > 14:
    discount = 0.20
    price_entire_stay_studio =  price_entire_stay_studio * (1 - discount)

if number_of_overnight > 14:
    discount = 0.10
    price_entire_stay_apartment =  price_entire_stay_apartment * (1 - discount)

print(f"Apartment: {price_entire_stay_apartment:.2f} lv.")
print(f"Studio: {price_entire_stay_studio:.2f} lv.")
