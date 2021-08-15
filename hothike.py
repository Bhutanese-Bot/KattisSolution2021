number_of_days = int(input())
days = list(map(int,input().split(' ')))
day1 = 0
day2 = 0
check = []
d = []
for i in range(0,len(days)):
	new = days[i:i+3]
	if len(new) == 3:
		check.append(abs(new[2] - new[0]))
		ans = [abs(new[2] - new[0]),new]
		d.append(ans)
check = min(check)
n = []
day_to_start = 0
for item in d:
	if item[0] == check:
		s = item[1][0] + item[1][2]
		n.append(s)
n = min(n)
m=0
for item in d:
	if item[0] == check:
		s = item[1][0] + item[1][2]
		if s == n:
			if day_to_start == item[1][0] or day_to_start == item[1][2] or m == item[1][0] or m == item[1][2]:
				pass
			else:
				day_to_start = item[1][0]
				if item[1][2] > item[1][0]:
					m = item[1][2]
				else:
					m = item[1][0]
for i in range(0,len(days)):
	if days[i] == day_to_start:
		day_to_start = i+1
		break
print(str(day_to_start),str(m))


