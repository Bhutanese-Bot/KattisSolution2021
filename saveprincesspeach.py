obstacles,obs = map(int,input().split(' '))
List = []
for i in range(obs):
	List.append(int(input()))
List = set(List)
Length = len(List)
List = list(List)
for i in range(0,obstacles):
	if i in List:
		pass
	else:
		print(i)
print(f'Mario got {Length} of the dangerous obstacles.')