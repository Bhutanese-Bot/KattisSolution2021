for i in  range(int(input())):
	List = list(map(int,input().split(' ')))
	List.remove(List[-1])
	ans = 0
	for i in range(1,len(List)):
		if List[i] > (2*List[i-1]):
			ans += (List[i] - (2*List[i-1]))
	print(ans)