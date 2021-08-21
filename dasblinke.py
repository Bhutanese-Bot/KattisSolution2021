p,q,s = input().split(' ')
indexes_of_p = [int(i) for i in range(0,int(s)+1,int(p))]
indexes_of_p.remove(indexes_of_p[0])
indexes_of_q = [int(i) for i in range(0,int(s)+1,int(q))]
indexes_of_q.remove(indexes_of_q[0])
List_of_p = []
List_of_q = []
for i in range(1,int(s)+1):
	if i in indexes_of_p:
		List_of_p.append('W')
	else:
		List_of_p.append('B')

	if i in indexes_of_q:
		List_of_q.append('W')
	else:
		List_of_q.append('B')
count = 0
for i in range(0,len(List_of_q)):
	if List_of_p[i] == List_of_q[i] and List_of_p[i] != 'B' and List_of_q[i] != 'B' :
		count += 1
if count > 0:
	print('yes')
else:
	print('no')