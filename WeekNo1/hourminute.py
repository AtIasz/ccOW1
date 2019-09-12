first_hour=int (input("Hour number A: "))
first_minutes=int(input("Minute number A: "))
first_seconds=int (input("Second number A: "))
second_hour=int (input("Hour number B: "))
second_minutes=int(input("Minute number B: "))
second_seconds=int(input("Second number B: "))

if first_hour>second_hour:
 hourDiff=first_hour-second_hour

else:
 hourDiff=second_hour-first_hour

if first_minutes>second_minutes:
 minutesDiff=first_minutes-second_minutes

else:
 minutesDiff=second_minutes-first_minutes

if first_seconds>second_seconds:
 secondsDiff=first_seconds-second_seconds

else:
 secondsDiff=second_seconds-first_seconds

print(secondsDiff+(minutesDiff*60)+(hourDiff*3600))
