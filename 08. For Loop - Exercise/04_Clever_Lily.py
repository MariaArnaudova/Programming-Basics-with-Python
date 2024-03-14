age = int(input())
washmachine_price = float(input())
toy_price = int(input())

savings = 0
toys_count = 0
years_count = 0

for year in range(1, age + 1):
    if year % 2 == 0:
        savings += 10 * (years_count + 1)
        savings -= 1
        years_count += 1
    elif year % 2 == 1:
        toys_count += 1

toys_money = toys_count * toy_price

lylys_earns = toys_money + savings
needed_money = abs(washmachine_price - lylys_earns)

if lylys_earns >= washmachine_price:
    print(f'Yes! {needed_money:.2f}')
else:
    print(f'No! {needed_money:.2f}')
