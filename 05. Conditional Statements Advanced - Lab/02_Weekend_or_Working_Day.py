day_input = input()
output = ''

if day_input == "Monday" \
        or day_input == "Tuesday" \
        or day_input == "Wednesday" \
        or day_input == "Thursday" \
        or day_input == "Friday":
    output = 'Working day'
elif day_input == "Saturday" or day_input == "Sunday":
    output = 'Weekend'
else:
    output = 'Error'

print(output)
