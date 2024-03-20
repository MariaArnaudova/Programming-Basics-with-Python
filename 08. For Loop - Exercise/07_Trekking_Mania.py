groups_number = int(input())

percent_musala = 0.0
percent_montblan = 0.0
percent_kilimanjaro = 0.0
percent_k2 = 0.0
percent_everest = 0.0

total_number_of_people = 0

for i in range(1, groups_number + 1):
    people_in_group = int(input())
    total_number_of_people += people_in_group
    if people_in_group <= 5:
        percent_musala += people_in_group
    elif 6 <= people_in_group <= 12:
        percent_montblan += people_in_group
    elif 13 <= people_in_group <= 25:
        percent_kilimanjaro += people_in_group
    elif 26 <= people_in_group <= 40:
        percent_k2 += people_in_group
    elif people_in_group >= 41:
        percent_everest += people_in_group

percent_musala = (percent_musala / total_number_of_people) * 100
percent_montblan = (percent_montblan / total_number_of_people) * 100
percent_kilimanjaro = (percent_kilimanjaro / total_number_of_people) * 100
percent_k2 = (percent_k2 / total_number_of_people) * 100
percent_everest = (percent_everest / total_number_of_people) * 100

print(f'{percent_musala:.2f}%')
print(f'{percent_montblan:.2f}%')
print(f'{percent_kilimanjaro:.2f}%')
print(f'{percent_k2:.2f}%')
print(f'{percent_everest:.2f}%')
