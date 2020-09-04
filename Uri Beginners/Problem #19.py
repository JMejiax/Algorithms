# Beginner - Problem #17

time_in_seconds = int(input())
if time_in_seconds < 60:
	print("0:0:"+str(time_in_seconds))

if time_in_seconds > 59:
	seconds = time_in_seconds%60
	time_in_minutes = (time_in_seconds - seconds) / 60
	if time_in_minutes > 59:
		minutes = time_in_minutes%60
		hours = (time_in_minutes - minutes) / 60
		print(str(hours).replace(".0", "")+":"+str(minutes).replace(".0", "")+":"+str(seconds))
	else:
		print("0:"+str(time_in_minutes).replace(".0", "")+":"+str(seconds))


