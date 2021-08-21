import math as m
for i in range(int(input())):
	v,angle,x,h1,h2 = map(float,input().split(' '))
	angle = (m.pi*angle)/180
	t = x/(v*m.cos(angle))
	y = (v*t*m.sin(angle)) - (0.5*9.8*pow(t,2)) 
	h1 = h1 + 1
	print(y)
	if h1 <= y <= h2-1: 
		print('Safe')
	else:
		print('Not Safe')