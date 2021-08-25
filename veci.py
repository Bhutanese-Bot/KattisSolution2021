number = input()
check = int(number)
nu = sorted(number,reverse=True)
nu = ''.join(nu)
if number == nu:
	print(0)
else:
	while True:
		check += 1
		if sorted(str(check)) == sorted(str(number)):
			print(check)
			break
