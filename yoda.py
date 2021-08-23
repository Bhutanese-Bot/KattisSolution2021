num1 = list(input())
num2 = list(input())
num1 = num1[::-1]
num2 = num2[::-1]
for i in range(0,len(num1)):
	try:
		if int(num1[i]) > int(num2[i]):
			num2[i] = '.'
		elif int(num1[i]) == int(num2[i]):
			pass
		else:
			num1[i] = '.'
	except IndexError:
		break
num1 = [item for item in num1[::-1] if item != '.']
num2 = [item for item in num2[::-1] if item != '.']
if len(num1) != 0:
	if num1[0] == '0':
		num1 = '0'
if len(num2) != 0:
	if num2[0] == '0' and len(num2) != 0:
		num2 = '0'
print('YODA') if len(num1) == 0 else print(''.join(num1))
print('YODA') if len(num2) == 0 else print(''.join(num2))
