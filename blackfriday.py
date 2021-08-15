number = int(input())
Dict = {}
List = list(map(int,input().split(' ')))
count = 0
ans = 0
for item in List:
	if item not in Dict:
		Dict[item] = 1
	else:
		Dict[item] += 1
for k in sorted(Dict,reverse=True):
	if Dict[k] == 1:
		count = k
		break
if count > 0:
	print(List.index(count)+1)
else:
	print('none')