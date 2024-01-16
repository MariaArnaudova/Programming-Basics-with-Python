# 1. Необходимо количество найлон (в кв.м.) - цяло число в интервала [1... 100]
nylon_count = int(input())
paint_ltr = int(input())
thinner = int(input())
hours_work = int(input())

protective_nylon_price = 1.50
paint_price = 14.50
paint_thinner_price = 5.00
nylon_price = 2
bags_price = 0.40

sum_nylon = (nylon_count + 2) * protective_nylon_price
sum_paint_price = (paint_ltr * 1.1) * paint_price
sum_thinner = thinner * paint_thinner_price
sum_bags = bags_price

all_price_materials = sum_nylon + sum_paint_price + sum_thinner + sum_bags
amount_per_master = (all_price_materials * 0.3) * hours_work
final_price = amount_per_master + all_price_materials

print(final_price)
