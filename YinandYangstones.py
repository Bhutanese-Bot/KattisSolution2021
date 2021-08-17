def readarray(x):
	return list(x)
stones = readarray(input())
print(1) if stones.count('W') == stones.count('B') else print(0)
