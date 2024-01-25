peters_budget = float(input())
number_video_cards = int(input())
number_processors = int(input())
number_ram = int(input())

# Ако броя на видеокартите е по-голям от този на процесорите получава 15% отстъпка от крайната сметка. Важат следните цени:
# •	Видеокарта – 250 лв./бр.
# •	Процесор – 35% от цената на закупените видеокарти/бр.
# •	Рам памет – 10% от цената на закупените видеокарти/бр.
# Да се изчисли нужната сума за закупуване на материалите и да се пресметне дали бюджета ще му стигне.
video_card_price = 250
processor_price = 0.35 * (number_video_cards * video_card_price)
ram_price = 0.10 * (number_video_cards * video_card_price)

price_ordered_video_cards = number_video_cards * video_card_price
price_ordered_processors = number_processors * processor_price
price_ordered_ram = number_ram * ram_price

amount = price_ordered_video_cards + price_ordered_processors + price_ordered_ram

if number_video_cards > number_processors:
    amount -= 0.15 * amount

residual_budget = peters_budget - amount
needed_amount = amount - peters_budget

if amount <= peters_budget:
    print(f'You have {residual_budget:.2f} leva left!')
else:
    print(f'Not enough money! You need {needed_amount:.2f} leva more!')

