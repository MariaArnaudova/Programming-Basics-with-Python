travel_price = float(input())
puzzles_count = int(input())
talking_doll_count = int(input())
teddy_bear_count = int(input())
mignon_count = int(input())

trucks_count = int(input())

puzzle_price = 2.60
talking_doll_price = 3
teddy_bear_price = 4.10
mignon_price = 8.20
truck_price = 2
rent = 0.10

toys_sum = puzzles_count + talking_doll_count + teddy_bear_count + mignon_count + trucks_count
toys_price = puzzles_count * puzzle_price + \
             talking_doll_count * talking_doll_price + \
             teddy_bear_count * teddy_bear_price + \
             mignon_count * mignon_price + \
             trucks_count * truck_price

if toys_sum >= 50:
    toys_price -= (toys_price * 0.25)
    # toys_price_with_discount = toys_price * (1 - 0.25)

toys_price -= (rent * toys_price)
# toys_profit = toys_price_with_discount * (1 - 0.10)
money_needed = travel_price - toys_price
money_left = toys_price - travel_price

if toys_price >= travel_price:
    print(f"Yes! {money_left:.2f} lv left.")
else:
    print(f"Not enough money! {money_needed:.2f} lv needed.")
