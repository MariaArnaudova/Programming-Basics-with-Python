import math

number_of_tournaments = int(input())
initial_number_of_points_ranking_list = int(input())

final_points = 0
final_points += initial_number_of_points_ranking_list
arevage_points_in_tour = 0
percent_won_tours = 0
tournaments_won = 0

for i in range(1, number_of_tournaments + 1):
    stage_reached = input()

    if stage_reached == 'W':
        final_points += 2000
        tournaments_won += 1
    elif stage_reached == 'F':
        final_points += 1200
    elif stage_reached == 'SF':
        final_points += 720

arevage_points_in_tour = (final_points - initial_number_of_points_ranking_list)/ number_of_tournaments
percent_won_tours = (tournaments_won / number_of_tournaments) * 100

print(f'Final points: {final_points}')
print(f'Average points: {math.floor(arevage_points_in_tour)}')
print(f'{percent_won_tours:.2f}%')
