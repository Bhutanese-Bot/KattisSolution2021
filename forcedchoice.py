number, secret , loop = map(int,input().split())
for i in range(0,loop):
	number = list(map(int,input().split(' ')))
	number.remove(number[0])
	if secret in number:
		print('KEEP')
	else:
		print('REMOVE')