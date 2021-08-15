testcase = int(input())
for i in range(testcase):
	line = input()
	loops = int(input())
	List = []
	for i in range(loops):
		List.append(int(input()))
	s = sum(List)
	div = s // loops
	new_sum = 0
	for i in range(loops):
		new_sum += div
	if new_sum == s:
		print('YES')
	else:
		print('NO')