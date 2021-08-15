def encode(text,rotate_pos):
	alphabet = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
	new_alphabet = []
	if (alphabet.index(text)+rotate_pos) <= alphabet.index(alphabet[-1]):
		return alphabet[rotate_pos+alphabet.index(text)]
	try:
		return alphabet[(rotate_pos+alphabet.index(text))-len(alphabet)]
	except IndexError:
		return alphabet[(rotate_pos+alphabet.index(text))-2*(len(alphabet))]
alphabet = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
text = input()
number = len(text)
midpoint = number / 2
text1 = text[0:int(midpoint)]
text2 = text[int(midpoint):]
count1 = 0
count2 = 0
for i in range(0,len(text1)):
	count1 += alphabet.index(text[i])
for i in range(0,len(text2)):
	count2 += alphabet.index(text[i])
print(count1)
print(count2)
List1 = []
List2 = []
for i in range(0,len(text1)):#for rotate

	List1.append(encode(text1[i],count1))
for i in range(0,len(text2)):#for rotate
	List2.append(encode(text2[i],count2))
print(List1)
print(List2)