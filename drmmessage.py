from string import ascii_uppercase as alphabets
from functools import reduce
letters = input()
to_div = len(letters) // 2
let_1 = letters[:to_div]
let_2 = letters[to_div:]
rot_1 = 0
rot_2 = 0
for item in list(let_1):
	rot_1 += alphabets.index(item)
for item in list(let_2):
	rot_2 += alphabets.index(item)
def rotate(letter,pos_value):
	des_rot = alphabets.index(letter) + pos_value
	factor = des_rot // len(alphabets)
	if des_rot <= len(alphabets)-1:
		return alphabets[des_rot]
	return alphabets[des_rot - (factor*len(alphabets))]
first = ''
second = ''
for item in list(let_1):
	first += rotate(item,rot_1)
for item in list(let_2):
	second += rotate(item,rot_2)
new = ''
for i in range(0,len(first)):
	new += rotate(first[i],alphabets.index(second[i]))
print(new)
