annual_fee_basketball_training = int(input())

sneakers_price = annual_fee_basketball_training * (1 - 0.4)
equipment_price = sneakers_price * (1 - 0.2)
ball_price = 1 / 4 * equipment_price
accessories_price = 1 / 5 * ball_price

all_price_equipment = annual_fee_basketball_training + sneakers_price + equipment_price + ball_price + \
                      accessories_price

print(all_price_equipment)
