budget = int(input())
season = input()
fishermen_count = int(input())

boat_rent = 0

left_money = 0.0
money_for_rent = 0.0

if season == 'Spring':
    boat_rent = 3000
elif season == 'Summer' or season == 'Autumn':
    boat_rent = 4200
elif season == 'Winter':
    boat_rent = 2600

discount = 0

if fishermen_count <= 6:
    discount = 0.1
elif fishermen_count <= 11:
    discount = 0.15
elif fishermen_count >= 12:
    discount = 0.25

next_discount = 0

if fishermen_count % 2 == 0 and season != 'Autumn':
    next_discount = 0.05

money_for_rent = boat_rent * (1 - discount) * (1 - next_discount)
left_money = budget - money_for_rent
needed_money = money_for_rent - budget

if left_money >= 0:
    print(f"Yes! You have {left_money:.2f} leva left.")
else:
    print(f"Not enough money! You need {needed_money:.2f} leva.")
