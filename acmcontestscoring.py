List = []
total = 0
solved = 0
while True:
	log = input()
	if log == '-1':
		break
	else:
		List.append(log)
		minutes,que,state = log.split(' ')
		if state == 'right':
			for item in List:
				if que in item and item.endswith('wrong'):
					total = total + 20
			total = total + int(minutes)
			solved = solved + 1
print(str(solved)+' '+ str(total))



