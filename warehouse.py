testCase = int(input())
for i in range(0,testCase):
	N = int(input())
	myDict = {}
	newDict = {}
	for i in range(0,N):
		toy,number = input().split(' ')
		if toy not in myDict:
			myDict[toy] = int(number)
		else:
			myDict[toy]+= int(number)
	for k,v in myDict.items():
		newDict.setdefault(v,[]).append(k)
	print(len(myDict))
	for k in sorted(newDict,reverse=True):
		for item in sorted(newDict[k]):
			print(item +' '+ str(k))