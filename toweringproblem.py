from itertools import permutations as p
from sys import exit
List = list(map(int,input().split(' ')))
tower_2 = List.pop()
tower_1 = List.pop()
while True:
    new = list(p(List,len(List)))
    for item in new:
        item = list(item)
        one = item[:len(item)//2]
        two = item[len(item)//2:]
        if sum(one) == tower_1 and sum(two) == tower_2:
            print(*(sorted(one,reverse=True)),*(sorted(two,reverse=True)))
            exit(0)
