from string import ascii_uppercase as au
def decode(key,word):
	alpha = list(au)
	text = ''
	key = list(key)
	word = list(word)
	for i in range(0,len(key)):
		try:
			shift = alpha.index(word[i])-alpha.index(key[i])
			text  += alpha[shift]
		except IndexError:
			pass
	return text
cipher_text = input()
key = input()
ans = ''
cipher_text = [cipher_text[i:i+len(key)] for i in range(0,len(cipher_text),len(key))]
for i in range(0,len(cipher_text)):
	text = decode(key,cipher_text[i])
	ans += text
	key = text
print(ans)
