budget = int(input())
season = input()
fishermen_count = int(input())

spring_rent = 3000
summer_autumn_rent = 4200
winter_rent = 2600

left_money = 0.0
needed_money = 0.0

if season == 'Spring':
    if fishermen_count <= 6:
        budget = budget - spring_rent * (1 - 0.1)
    elif fishermen_count <= 11:
        budget = budget - spring_rent * (1 - 0.15)
    elif fishermen_count >= 12:
        budget = budget - spring_rent * (1 - 0.25)
    if fishermen_count % 2 == 0:
        # budget -= spring_rent * 0.05
            budget = budget - spring_rent * (1 - 0.05)
elif season == 'Summer' or season == 'Autumn':
    if fishermen_count <= 6:
        budget = budget - summer_autumn_rent * (1 - 0.1)
    elif fishermen_count <= 11:
        budget = budget - summer_autumn_rent * (1 - 0.15)
    elif fishermen_count >= 12:
        budget = budget - summer_autumn_rent * (1 - 0.25)
    if season == 'Summer' and fishermen_count % 2 == 0:
            # budget -= summer_autumn_rent * 0.05
            budget = budget - summer_autumn_rent * (1 - 0.05)
elif season == 'Winter':
    if fishermen_count <= 6:
        budget = budget - winter_rent * (1 - 0.1)
    elif fishermen_count <= 11:
        budget = budget - winter_rent * (1 - 0.15)
    elif fishermen_count >= 12:
        budget = budget - winter_rent * (1 - 0.25)
    if fishermen_count % 2 == 0:
        # budget -= winter_rent * 0.05
         budget = budget - winter_rent * (1 - 0.05)

needed_money = abs(budget)

if budget >= 0:
    print(f"Yes! You have {budget:.2f} leva left.")
else:
    print(f"Not enough money! You need {needed_money:.2f} leva.")
