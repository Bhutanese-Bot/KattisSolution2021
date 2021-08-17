Dict = {}
while True:
	name = input()
	if name == '***':
		break
	else:
		if name not in Dict:
			Dict[name] = 1
		else:
			Dict[name] += 1
values = [v for k,v in Dict.items()]
m = max(values)
values = [ k for k,v in Dict.items() if v == m ]
print(values[0]) if len(values) == 1 else print('Runoff!')