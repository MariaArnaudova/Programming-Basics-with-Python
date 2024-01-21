number = int(input())

bonus_points = 0

if number % 2 == 0:
    bonus_points += 1
elif number % 10 == 5:
    bonus_points += 2

if number <= 100:
    bonus_points += 5
elif number > 1000:
    bonus_points += 0.1 * number
else:
    bonus_points += 0.2 * number

final_number = number + bonus_points

print(f'{bonus_points}\n{final_number}')
