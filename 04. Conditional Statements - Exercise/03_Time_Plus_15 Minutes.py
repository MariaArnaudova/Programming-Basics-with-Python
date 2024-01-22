hours = int(input())
minutes = int(input())

reload_minutes = minutes + 15

if reload_minutes > 59:
    minutes = reload_minutes - 60
    hours += 1
    if hours == 24:
        hours = 0
else:
    minutes = reload_minutes


if minutes < 10:
    minutes = f"{minutes:02d}"

print(f"{hours}:{minutes}")
