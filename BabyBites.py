num = int(input())
List = []
new_List = []
count = 0
List = input().split(' ')
index = 0
for item in List:
	index = index + 1
	if 'mumble' in item:
		new = item.replace('mumble',str(index))
		new_List.append(new)
	else:
		new_List.append(item)
compare = [str(i) for i in range(1,num+1)]
for i in range(0,num):
	if new_List[i] != compare[i]:
		count = count + 1
if count != 0:
	print('something is fishy')
else:
	print('makes sense')


