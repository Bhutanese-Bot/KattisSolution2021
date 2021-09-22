def fact(n):
	s = 1
	for i in range(2,n+1):
		s = s * i
	return s
num  = int(input())
s = 0
for i in range(2,num+1):
	s += (fact(num)//(fact(i)*(fact(num-i))))#Use Combinations fmla or use itertools 
print(s)
