n = int(input())
left_sum = 0
right_sum = 0

for i in range(1, n + 1):
    current_number = int(input())
    left_sum += current_number

for i in range(1, n + 1):
    current_number = int(input())
    right_sum += current_number


difference = abs(left_sum - right_sum)

if left_sum == right_sum:
    print(f'Yes, sum = {left_sum}')
else:
    print(f'No, diff = {difference}')
