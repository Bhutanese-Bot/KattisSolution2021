#time complexity = 0(n^2.C)
testcase = int(input())
for i in range(testcase):
	count = 0
	List = []
	number_of_days,month = map(int,input().split(' '))
	month = list(map(int,input().split(' ')))
	for item in month:
		List.extend(list(range(1,item+1)))
	List = [List[j:j+7]for j in range(0,len(List),7)]
	for s in range(0,len(List)):
		if 13 in  List[s]:
			if List[s].index(13) == 5:
				count += 1
	print(count)
