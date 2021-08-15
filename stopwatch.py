test_case = int(input())
List = []
for i in range(test_case):
	List.append(int(input()))
if test_case % 2 != 0:
	print('still running')
else:
	display = 0
	for i in range(0,test_case):
		if (i+1) % 2 == 0:
			display += List[i] - List[i-1]
	print(display)
 