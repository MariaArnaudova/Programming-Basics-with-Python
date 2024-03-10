import sys

number = int(input())

max_number = - sys.maxsize
sum_all_numbers = 0
bigger_number = max_number

for i in range(0, number):
    current_number = int(input())
    if current_number > bigger_number:
        bigger_number = current_number
    sum_all_numbers += current_number

if bigger_number == sum_all_numbers - bigger_number:
    print('Yes')
    print(f'Sum = {bigger_number}')
else:
    sum_all_numbers = sum_all_numbers - bigger_number
    print('No')
    print(f'Diff = {abs(sum_all_numbers - bigger_number)}')


