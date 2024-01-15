from math import  floor

pages_count = int(input())
pages_per_hours = int(input())
days_count = int(input())

total_hours = pages_count / pages_per_hours
hours_per_day = total_hours / days_count
print(floor(hours_per_day))
