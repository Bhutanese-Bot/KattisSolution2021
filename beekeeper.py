while True:
	number = int(input())
	if number == 0:
		break
	else:
		mydict = {}
		List = []
		vowel =['a','e','i','o','u','y']
		for i in range(0,number):
			List.append(input())
		for item in List:
			check = list(item)
			count = 0
			for j in range(1,len(check)):
				if check[j] in vowel and check[j] == check[j-1]:
					count+=1
				mydict[item] = count
		Li = []
		for k,v in mydict.items():
			Li.append(v)
		num = max(Li)
		for k in mydict:
			if mydict[k] == num:
				print(k)