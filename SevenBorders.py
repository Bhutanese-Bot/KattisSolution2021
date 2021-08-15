import string
Letters = input()
small = list(string.ascii_lowercase)
capital = string.ascii_lowercase
Capital = list(capital.upper())
Space = '_'
total = len(Letters)
S = 0
C = 0
U = 0
Symbols = 0
for item in Letters:
	if item in small:
		S = S + 1
	elif item in Capital:
		C = C + 1
	elif item == Space:
		U = U + 1
	else:
		Symbols = Symbols + 1
print(U/total)
print(S/total)
print(C/total)
print(Symbols/total)



