correct_guess = 0
incorrect = 0
word = list(input())
permutation = list(input())
for i in range(0,len(permutation)):
	if permutation[i] in word:
		correct_guess += word.count(permutation[i])
	if correct_guess == len(word):
		print('WIN')
		break
	if permutation[i] not in word:
		incorrect += 1
	if incorrect == 10:
		print('LOSE')
		break