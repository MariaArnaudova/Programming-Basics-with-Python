time = int(input())
day = input()

if time >= 10 and time <= 18:
    if day != 'Sunday':
        print('open')
    else:
        print('closed')
else:
    print('closed')