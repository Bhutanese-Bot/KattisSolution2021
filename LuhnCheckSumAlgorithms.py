num = int(input())
get = []
for i in range(0,num):
	number = input()
	new = number[::-1]
	List = [new[i:i+2]for i in range(0,len(new),2)]
	count = 0
	for item in List:
		single = 0
		if len(item)>1:
			count = count + int(item[0])
			try:
				if len(str(int(item[1]*2))) > 1:
					num = int(item[1])*2
					while  num != 0:
						rem = num % 10
						single = single + rem
						num = num //10
					count = count + single
				else:
					count = count + 2 * int(item[1])
			except IndexError:
				pass
		else:
			count = count + int(item[0])
	if count % 10 == 0:
		get.append('PASS')
	else:
		get.append('FAIL')
for item in get:
	print(item)
