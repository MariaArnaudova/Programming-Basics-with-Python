actor_name = input()
academy_points = float(input())
number_of_assessors = int(input())

evaluation = 0
evaluation += academy_points

for i in range(1, number_of_assessors + 1):
    name = input()
    points = float(input())
    len_name = len(name)
    evaluation += (len_name * points) / 2
    if evaluation >= 1250.50:
        print(f'Congratulations, {actor_name} got a nominee for leading role with {evaluation:.1f}!')
        break

needed_evaluation = 1250.50 - evaluation

if evaluation < 1250.50:
    print(f'Sorry, {actor_name} you need {needed_evaluation:.1f} more!')
