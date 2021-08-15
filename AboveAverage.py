number = int(input())
for i in range(0,number):
	total = 0
	numbers = input().split(' ')
	divisor = numbers.pop(0)
	for item in numbers:
		total = total + int(item)
	average = total / int(divisor)
	count = 0
	for item in numbers:
		if int(item) > average:
			count = count + 1
	final = format((count/int(divisor))*100,".3f")
	print(final+'%')





