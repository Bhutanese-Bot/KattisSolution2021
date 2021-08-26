shattered_pieces = int(input())
List = list(map(int,input().split(' ')))
A = 0
B = 0
List = sorted(List,reverse=True)
for i in range(0,len(List)):
	if (i+1) % 2 != 0:
		A += List[i]
	else:
		B += List[i]
print(A, B)