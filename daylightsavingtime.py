Testcase = int(input())
for i in range(Testcase):
	F_or_B,pos,hour,minutes = input().split(' ')
	pos = int(pos)
	hour = int(hour)
	minutes = int(minutes)
	if F_or_B == 'F':
		total = minutes + pos
		if total > 60:
			total = total - 60
			minutes = total
			hour += 1
		elif total == 60:
			minutes = 0
			hour += 1
		else:
			minutes = total
		if minutes > 60:
			minutes -= 60
			hour += 1
		if minutes == 60:
			minutes = 0
			hour += 1
		if hour == 24:
			hour = 0
		text = str(hour) +' '+ str(minutes)
		print(text)
	else:
		text = ''
		total = minutes - pos
		if total < 0:
			if hour == 0:
				hour+= 24
			minutes += 60
			hour = hour - 1
			minutes -= pos
		else:
			minutes = total
		if minutes < 0:
			if hour == 0:
				hour+= 24
			minutes += 60
			hour = hour - 1
		if hour == 24:
			hour = 0
		text = str(hour) +' '+str(minutes)
		print(text)
