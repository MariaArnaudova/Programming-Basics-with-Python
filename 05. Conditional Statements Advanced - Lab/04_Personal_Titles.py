age = float(input())
gender = input()
output = ''

if age >= 16:
    if gender == 'm':
        output = "Mr."
    elif gender == 'f':
        output = "Ms."

if age < 16:
    if gender == 'm':
        output = "Master"
    elif gender == 'f':
        output = "Miss"

print(output)
