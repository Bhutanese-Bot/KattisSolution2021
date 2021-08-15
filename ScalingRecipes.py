from collections import defaultdict
testcase = int(input())
for l in range(0,testcase):
	loop,main,desired = map(int,input().split(' '))
	check_name = ''
	Dict = defaultdict(list)
	scaling_factor = desired / main
	for i in range(loop):
		name,weight,percentage = input().split(' ')
		weight = float(weight)
		percentage = float(percentage)
		if percentage == 100.0:
			check_name = name
		Dict[name].append(weight)
		Dict[name].append(percentage)
	main_scaled_weight = Dict[check_name][0] * scaling_factor
	answer = {}
	for item in Dict:
		answer[item] = main_scaled_weight * (Dict[item][1]/100)
	print(f'Recipe # {l+1}')
	for k,v in answer.items():
		v = '%.1f'%v
		print(k,str(v))
	print('-'*40)





