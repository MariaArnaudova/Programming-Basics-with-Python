budget = float(input())
season = input()

destination = ''
spended_money = 0.0
vacantion_place = ''

if budget <= 100:
    destination = 'Bulgaria'
elif budget <= 1000:
    destination = 'Balkans'
elif budget > 1000:
    destination = 'Europe'

if season == 'summer' and destination =='Bulgaria':
    spended_money = 0.30 * budget
    vacantion_place = 'Camp'
elif season == 'winter' and destination =='Bulgaria':
    spended_money = 0.70 * budget
    vacantion_place = 'Hotel'
elif season == 'summer' and destination =='Balkans':
    spended_money = 0.40 * budget
    vacantion_place = 'Camp'
elif season == 'winter' and destination =='Balkans':
    vacantion_place = 'Hotel'
    spended_money = 0.80 * budget
elif destination == 'Europe':
    spended_money = 0.90 * budget
    vacantion_place = 'Hotel'

print(f"Somewhere in {destination}")
print(f"{vacantion_place} - {spended_money:.2f}")



