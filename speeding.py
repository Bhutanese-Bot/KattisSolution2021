List = []
m = 0
for i in range(int(input())):
    time,dist = map(int,input().split(' '))
    List.append((time,dist))
for i in range(1,len(List)):
    try:
        speed = (List[i][1]-List[i-1][1]) / (List[i][0]-List[i-1][0])
        if speed > m:
           m = speed
    except ZeroDivisionError:
        pass
print(int(m))
