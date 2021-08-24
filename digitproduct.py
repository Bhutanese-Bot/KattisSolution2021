#used recursion instead iteration and it worked.
def summ(n):
	s = 1
	while n > 0:
		rem = n % 10
		if rem == 0:
			pass 
		else:
			s *= rem
		n = n // 10
	return s
def digit_product(n):
	n = summ(n)
	if len(str(n)) == 1:
		return n
	return digit_product(n)
number = int(input())
print(digit_product(number))
