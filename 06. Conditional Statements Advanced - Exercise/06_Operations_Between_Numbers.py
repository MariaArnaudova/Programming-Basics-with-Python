number_1 = int(input())
number_2 = int(input())
math_operator = input()

result = 0.0
difference = 0
even_or_odd = ''
message = ''

if math_operator == '+':
    result = number_1 + number_2
elif math_operator == '-':
    result = number_1 - number_2
elif math_operator == '*':
    result = number_1 * number_2
elif math_operator == '/' and number_2 != 0:
    result = number_1 / number_2
elif math_operator == '%' and number_2 != 0:
    difference = number_1 % number_2

if result % 2 == 0:
    even_or_odd = 'even'
else:
    even_or_odd = 'odd'

if math_operator == '+' \
        or math_operator == '-' \
        or math_operator == '*':
    message = f'{number_1} {math_operator} {number_2} = {result} - {even_or_odd}'
elif (math_operator == '/' or math_operator == '%') and number_2 == 0:
    message = f'Cannot divide {number_1} by zero'
elif math_operator == '/' and number_2 != 0:
    message = f'{number_1} / {number_2} = {result:.2f}'
elif math_operator == '%' and number_2 != 0:
    message = f'{number_1} % {number_2} = {difference}'

print(message)
