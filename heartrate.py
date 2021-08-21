testcase = int(input())
for i in range(testcase):
	b,p = map(float,input().split(' '))
	calc_bpm = (60*b)/p
	t = 60/p
	min_abpm = calc_bpm - t
	min_abpm = "%.4f"%min_abpm
	max_abpm = calc_bpm + t
	max_abpm =	"%.4f" % max_abpm
	calc_bpm = "%.4f" % calc_bpm
	print(min_abpm,calc_bpm,max_abpm)