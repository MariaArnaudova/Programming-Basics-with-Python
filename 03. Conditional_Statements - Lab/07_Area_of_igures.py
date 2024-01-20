from math import pi

figure = input()
area = 0

if figure == "square":
    side_one = float(input())
    area = side_one * side_one
elif figure == "rectangle":
    side_one = float(input())
    side_two = float(input())
    area = side_one * side_two
elif figure == "circle":
    radius = float(input())
    area = pi * radius ** 2
elif figure == "triangle":
    side_one = float(input())
    height = float(input())
    area = (side_one * height) / 2


print(f"{area:.3f}")
