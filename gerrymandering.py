from collections import defaultdict
def read(x):
	return map(int,x.split(' '))
pret,dist = read(input())
V = 0
wA = 0
wB = 0
Dict = defaultdict(list)
for i in range(pret):
	p,a,b = read(input())
	V += (a+b)
	if p not in Dict:
		Dict[p].append(a)
		Dict[p].append(b)
	else:
		Dict[p][0] += a
		Dict[p][1] += b
new = dict(Dict)
for k,v in sorted(new.items()):
	winner = ''
	if v[0] > v[1]:
		winner = 'A'
	else:
		winner = 'B'
	A = 0
	B = 0
	if v[0] > v[1]:
		A = v[0] - (((v[0]+v[1])//2) + 1)
		B = v[1]
	else:
		B = v[1] -(((v[0]+v[1])//2) + 1)
		A = v[0]
	wA += A
	wB += B
	print(f'{winner} {A} {B}')
E = (abs(wA-wB)) / V
print("%.6f" % E)

