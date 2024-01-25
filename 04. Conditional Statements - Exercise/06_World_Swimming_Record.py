import math

record_in_seconds = float(input())
distance_in_meters = float(input())
time_in_seconds = float(input())

water_resistance_for_15_metres = 12.5

distance_in_seconds = time_in_seconds * distance_in_meters
resistance_in_seconds_all_distance = math.floor(distance_in_meters / 15) * 12.5

all_time_for_swimming_Ivan = distance_in_seconds + resistance_in_seconds_all_distance
needed_seconds_for_record = all_time_for_swimming_Ivan - record_in_seconds

if all_time_for_swimming_Ivan < record_in_seconds:
    print(f'Yes, he succeeded! The new world record is {all_time_for_swimming_Ivan:.2f} seconds.')
else:
    print(f'No, he failed! He was {needed_seconds_for_record:.2f} seconds slower.')

