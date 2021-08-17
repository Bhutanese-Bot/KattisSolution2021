loop = int(input())
for i in range(loop):
	blankLine = input()
	Godzilla,MechaGodzilla = map(int,input().split(' '))
	G = list(map(int,input().split(' ')))
	M = list(map(int,input().split(' ')))
	winner = ''
	while True:
		cmpare = min(G + M)
		if cmpare in G and cmpare in M:
			M.remove(cmpare)
		else:
			M.remove(cmpare) if cmpare in M else G.remove(cmpare)
		if len(G) == 0:
			break
		if len(M) == 0:
			break
	if len(G) == 0:
		winner = 'MechaGodzilla'
	elif len(M) == 0 and len(G) == 0:
		winner = "Uncertain"
	else:
		winner = "Godzilla"
	print(winner)
