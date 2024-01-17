# Един литър вода се равнява на един кубичен дециметър/ 1л=1 дм3/.

length = int(input())
width = int(input())
height = int(input())
percentage = float(input())

volume_fish_tank = length * width * height
volume_ltr = volume_fish_tank * 0.001
occupied_spaces = percentage / 100

needed_litres_water = volume_ltr * (1 - occupied_spaces)

print(needed_litres_water)