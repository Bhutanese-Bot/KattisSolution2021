Adrian = ['A','B','C']
Bruno = ['B','A','B','C']
Goran = ['C','C','A','A','B','B']
List = []
b = 0
a = 0
g = 0
number = int(input())
word = input()
for_adrian = [word[i:i+3]for i in range(0,len(word),3)]
for_bruno = [word[i:i+4]for i in range(0,len(word),4)]
for_goran = [word[i:i+6]for i in range(0,len(word),6)]
for item in for_adrian:
	new = list(item)
	for i in range(0,len(new)):
		if new[i] == Adrian[i]:
			a += 1
			List.append('Adrian')
for item in for_bruno:
	new = list(item)
	for i in range(0,len(new)):
		if new[i] == Bruno[i]:
			count += 1
			List.append('Bruno')
for item in for_goran:
	new = list(item)
	for i in range(0,len(new)):
		if new[i] == Goran[i]:
			count += 1
			List.append('Goran')
print(count)
for item in sorted(set(List)):
	print(item)
