# По време на почивката отделяте време за обяд и време за отдих.
# Времето за обяд ще бъде 1/8 от времето за почивка,
# а времето за отдих ще бъде 1/4 от времето за почивка

# 1.	Име на сериал – текст
import math

film_name = input()
# 2.	Продължителност на епизод  – цяло число в диапазона [10… 90]
episode_duration = int(input())
# 3.	Продължителност на почивката  – цяло число в диапазона [10… 120]
rest_duration = int(input())

lunch_duration = 1/8 * rest_duration
leisure_duration = 1/4 * rest_duration

rest_time = episode_duration + lunch_duration + leisure_duration
left_time = rest_duration  - rest_time
needed_time = rest_time -  rest_duration

if rest_time <= rest_duration:
    print(f'You have enough time to watch {film_name} and left with {math.ceil(left_time)} minutes free time.')
else:
    print(f'You don\'t have enough time to watch {film_name}, you need {math.ceil(needed_time)} more minutes.')