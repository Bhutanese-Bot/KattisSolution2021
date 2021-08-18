no_of_items = int(input())
List = list(map(int,input().split(' ')))
List = sorted(List,reverse=True)
List = [List[i:i+3] for i in range(0,len(List),3)]
s = 0
for item in List:
	if len(item) == 3:
		s += min(item)
print(s)