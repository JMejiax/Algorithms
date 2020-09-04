
# Beginner - Problem #20
age_in_days = int(input())

if age_in_days < 30:
	print("0 ano(s)\n0 mes(es)\n" + str(age_in_days) + " dia(s)")
if age_in_days < 365:
	days = age_in_days%30
	age_in_months = (age_in_days - days) / 30
	print("0 ano(s)\n" + str(int(age_in_months)) + " mes(es)\n" + str(days) + " dia(s)")
	
if age_in_days > 364:
	days = age_in_days%365
	months = 0
	days_ = 0
	years = (age_in_days - days) / 365
	if days > 30:
		days_ = days%30
		months = (days - days_)/30
	print(str(int(years)) + " ano(s)\n" + str(int(months)) + " mes(es)\n" + str(days_) + " dia(s)")
		
