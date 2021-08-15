while True:
	number = int(input())
	if number == 0:
		break
	else:
		List =[]
		for loop in range(number):
			List.append(input())
		for i in range(0,len(List)):
			for j in range(0,len(List)-i-1):
				if List[j][:2] > List[j+1][:2]:
					List[j],List[j+1] = List[j+1],List[j]
				if List[j][:2] == List[j+1][:2]:
					pass
		for item in List:
			print(item)