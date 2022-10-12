import time

p1start = (8,35)
p1end = (9,18)
p2start = (9,21)
p2end = (10,1)
p3start = (10,4)
p3end = (10,44)
p4start = (10,47)
p4end = (11,27)
p5start = (11,30)
p5end = (12,10)
p6start = (12,13)
p6end = (12,53)
p7start = (12,56)
p7end = (13,36)
p8start = (13,39)
p8end = (14,9)
p9start = (14,12)
p9end = (14,52)
p10start = (14,55)
p10end = (15,35)

hour = int(time.strftime('%H'))
dayofweek = time.strftime('%a')
minute = int(time.strftime('%M'))
print(f"Today is {dayofweek}. The Time is {hour}:{minute}!")
currenttime = (hour,minute)
if currenttime[0] > p1start[0] and currenttime[1] > p1start[1]:
    period = 'beforeschool'
elif currenttime[0] < p1start[0] and currenttime[1] < p1start[1]:
    period = 'inschool'
else:
    period = 'Broken'

print(period)