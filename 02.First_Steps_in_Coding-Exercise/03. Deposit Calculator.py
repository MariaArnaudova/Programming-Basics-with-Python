# сума = депозирана сума + срок на депозита * ((депозирана сума * годишен лихвен процент ) / 12
deposit_sum = float(input())
deposit_term = int(input())
annual_interest_rate = float(input())

rate = deposit_sum * (annual_interest_rate/100)
month_rate = rate / 12
month_deposit_sum = deposit_sum + deposit_term * month_rate

#month_deposit_sum = deposit_sum + deposit_term * ((deposit_sum * (annual_interest_rate/100) / 12)

print(month_deposit_sum)
