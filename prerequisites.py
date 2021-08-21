while True:
	try:
		courses,category = map(int,input().split(' '))
		courses_selected = list(map(int,input().split(' ')))
		course = []
		for i in range(category):
			course_count,request,*course_numbers = map(int,input().split(' '))
			course.append((request,course_numbers))
		not_fulfilled = 0
		for item in course:
			add = 0
			for i in item[1]:
				if i in courses_selected:
					add += 1
			if add < item[0]:
				not_fulfilled += 1
		print('no') if not_fulfilled > 0 else print('yes')
	except ValueError:
		break

