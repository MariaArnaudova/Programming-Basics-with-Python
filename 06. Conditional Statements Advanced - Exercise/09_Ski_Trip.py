days_of_stay = int(input())
room_type = input()
evaluation = input()

discount = 0.0

room_for_one_person_price = 18.0
apartment_price = 25.0
president_apartment_price = 35.0

final_price = 0.0

if room_type == 'room for one person':
    final_price = (days_of_stay -1) * room_for_one_person_price
elif room_type == 'apartment':
    final_price = (days_of_stay -1)* apartment_price
    if days_of_stay <= 10:
        final_price = final_price * (1 - 0.30)
    elif days_of_stay > 10 and days_of_stay < 15:
        final_price = final_price * (1 - 0.35)
    elif days_of_stay >= 15:
        final_price = final_price * (1 - 0.50)
elif room_type == 'president apartment':
    final_price = (days_of_stay -1) * president_apartment_price
    if days_of_stay <= 10:
        final_price = final_price * (1 - 0.10)
    elif days_of_stay > 10 and days_of_stay < 15:
        final_price = final_price * (1 - 0.15)
    elif days_of_stay >= 15:
        final_price = final_price * (1 - 0.20)

if evaluation == 'positive':
    final_price += final_price * 0.25
elif evaluation == 'negative':
    final_price -= final_price * 0.10

print(f'{final_price:.2f}')
