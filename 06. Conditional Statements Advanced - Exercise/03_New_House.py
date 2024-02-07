flower = input()
number_flower = int(input())
budget = int(input())

rose_price = 5
dahlias_price = 3.80
tulip_price = 2.80
narcissus_price = 3
gladiolus_price = 2.50

final_price = 0.0

if flower == 'Roses':
    final_price = number_flower * rose_price
    if number_flower > 80:
        final_price -= final_price * 0.10
elif flower == 'Dahlias':
    final_price = number_flower * dahlias_price
    if number_flower > 90:
        final_price -= final_price * 0.15
elif flower == 'Tulips':
    final_price = number_flower * tulip_price
    if number_flower > 80:
        final_price -= final_price * 0.15
elif flower == 'Narcissus':
    final_price = number_flower * narcissus_price
    if number_flower < 120:
        final_price += final_price * 0.15
elif flower == 'Gladiolus':
    final_price = number_flower * gladiolus_price
    if number_flower < 80:
        final_price += final_price * 0.20

budget_sufficient = budget - final_price

if budget >= final_price:
    print(f'Hey, you have a great garden with {number_flower} {flower} and {budget_sufficient:.2f} leva left.')
else:
    print(f'Not enough money, you need {abs(budget_sufficient):.2f} leva more.')