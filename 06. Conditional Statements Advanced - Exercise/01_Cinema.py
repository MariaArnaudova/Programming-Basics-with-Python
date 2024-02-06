projection_type = input()
rows = int(input())
columns = int(input())

premiere_price = 12.00
normal_price = 7.50
discount = 5.00
seats_count = rows * columns
final_price = 0.0

if projection_type == 'Premiere':
    final_price = seats_count * premiere_price
elif projection_type == 'Normal':
    final_price = seats_count * normal_price
elif projection_type == 'Discount':
    final_price = seats_count * discount

print(f'{final_price:.2f}')
