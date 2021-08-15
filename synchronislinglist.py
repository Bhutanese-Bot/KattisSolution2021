while True:
	number = int(input())
	if number == 0:
		break
	else:
		List = []
		new = []
		for i in range(0,number*2):
			num = int(input())
			List.append(num)
		new = [List[i]for i in range(0,number)]
		new2 =[List[i]for i in range(number,len(List))]
		cmpare = sorted(new)
		cmpare2 = sorted(new2)
		insertion = sorted(new)
		for i in range(0,len(cmpare2)):
			answer = new.index(cmpare[i])
			insertion[answer] = cmpare2[i]
		for item in insertion:
			print(item)
		print()