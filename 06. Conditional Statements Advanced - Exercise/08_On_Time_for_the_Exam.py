# От конзолата се четат 4 цели числа (по едно на ред), въведени от потребителя:
# •	Първият ред съдържа час на изпита - цяло число от 0 до 23;
# •	Вторият ред съдържа минута на изпита - цяло число от 0 до 59;
# •	Третият ред съдържа час на пристигане - цяло число от 0 до 23;
# •	Четвъртият ред съдържа минута на пристигане - цяло число от 0 до 59.
hour_of_exam = int(input())
minute_of_exam = int(input())
arrival_hour = int(input())
arrival_minute = int(input())

arrival_minute - 30 < minute_of_exam
message = ''
minutes_before_start = minute_of_exam - arrival_minute

early_minutes = 60 - arrival_minute + minute_of_exam
if hour_of_exam - arrival_hour <= 1 and arrival_minute > minute_of_exam:
    message = f"Early\n{early_minutes} minutes before the start"

elif arrival_hour == hour_of_exam and arrival_minute == minute_of_exam:
    message = "On time"
elif (arrival_hour == hour_of_exam or hour_of_exam - arrival_hour == 1) and minute_of_exam == 00:
    message = f"on time {abs(60 - arrival_minute)} minutes before the start"
elif (arrival_hour == hour_of_exam or hour_of_exam - arrival_hour == 1) and minutes_before_start <= 30:
    message = f"on time {abs(minutes_before_start)} minutes before the start"

early_minutes = minute_of_exam - arrival_minute
if hour_of_exam > arrival_hour and early_minutes > 30:
    message = f'Early\n{hour_of_exam - arrival_hour}:{early_minutes:02d} hours before the start'

late_hours = arrival_hour - hour_of_exam
late_minutes = 60 - minute_of_exam + arrival_minute
if arrival_hour > hour_of_exam and arrival_minute < minute_of_exam:
    message = f"{late_hours}:{late_minutes:02d} hours after the start"

print(message)
