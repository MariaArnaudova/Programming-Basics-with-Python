# Град	0 ≤ s ≤ 500	 500 < s ≤ 1 000	1 000 < s ≤ 10 000	s > 10 000
# Sofia	5%	            7%	                8%	          12%
# Varna	4.5%	       7.5%	              10%	          13%
# Plovdiv	5.5%	   8%	             12%	            14.5%

city = input()
sales = float(input())
commission = 0.0
output_error = ''

if city == 'Sofia':
    if 0 <= sales and sales <= 500:
        commission = sales * 0.05
    elif 500 < sales and sales <= 1000:
        commission = sales * 0.07
    elif 1000 < sales and sales <= 10000:
        commission = sales * 0.08
    elif sales > 10000:
        commission = sales * 0.12
    else:
        output_error = 'error'
elif city == 'Varna':
    if 0 <= sales and sales <= 500:
        commission = sales * 0.045
    elif 500 < sales and sales <= 1000:
        commission = sales * 0.075
    elif 1000 < sales and sales <= 10000:
        commission = sales * 0.1
    elif sales > 10000:
        commission = sales * 0.13
    else:
        output_error = 'error'
elif city == 'Plovdiv':
    if 0 <= sales and sales <= 500:
        commission = sales * 0.055
    elif 500 < sales and sales <= 1000:
        commission = sales * 0.08
    elif 1000 < sales and sales <= 10000:
        commission = sales * 0.12
    elif sales > 10000:
        commission = sales * 0.145
    else:
        output_error = 'error'
else:
    output_error = 'error'

if output_error == 'error':
    print('error')
else:
    print(f'{commission:.2f}')
