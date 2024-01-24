budget_for_the_film = float(input())
number_of_extras = int(input())
price_for_clothing_of_one_extra = float(input())

if number_of_extras >= 150:
    price_for_clothing_of_one_extra -= 0.10 * price_for_clothing_of_one_extra

price_all_clothing = number_of_extras * price_for_clothing_of_one_extra
price_set_of_film = 0.10 * budget_for_the_film

all_money_for_film = price_all_clothing + price_set_of_film
needed_money = all_money_for_film - budget_for_the_film
left_money = budget_for_the_film - all_money_for_film

if all_money_for_film > budget_for_the_film:
    print(f"Not enough money!\nWingard needs {needed_money:.2f} leva more.")
elif all_money_for_film <= budget_for_the_film:
    print(f"Action!\nWingard starts filming with {left_money:.2f} leva left.")
