letter = list(input())
main_word = letter[0]
Dict = []
num = int(input())
for i in range(num):
	word = list(input())
	if len(word) >= 4:
		flag = [i in letter for i in word]
		if False not in flag:
			if main_word in word:
				print(''.join(word))
