import sys

smallest_num = sys.maxsize
biggest_num = - sys.maxsize

number = int(input())

for i in range(0, number):
    num = int(input())
    if num < smallest_num:
        smallest_num = num
    if num > biggest_num:
        biggest_num = num

print(f'Max number: {biggest_num}')
print(f'Min number: {smallest_num}')
