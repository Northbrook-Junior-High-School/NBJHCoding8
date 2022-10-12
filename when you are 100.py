import datetime

age = int(input("How old are you?: "))
dte = datetime.date.today()
current_year = dte.year
years_till_100 = 100 - age
print("You will be 100 in the year " + str(current_year + years_till_100))
