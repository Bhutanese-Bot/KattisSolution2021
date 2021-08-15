Boat_Parts, number_of_days = input().split(' ')
List = []
core = 0
new_List = []
for i in range(0,int(number_of_days)):
	boatParts = input()
	List.append(boatParts)
check = set(List)
if int(Boat_Parts) != len(check):
	print('paradox avoided')
else:
	for item in List:
		if item not in new_List:
			new_List.append(item)
		else:
			pass
	core = new_List[-1]
	print(List.index(core)+1)
