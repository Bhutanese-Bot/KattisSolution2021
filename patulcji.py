from itertools import permutations as pt
numbers = []
for i in range(9):
	numbers.append(int(input()))
brute_list = pt(numbers,7)
for item in brute_list:
	if sum(item) == 100:
		for values in item:
			print(values)
		break

