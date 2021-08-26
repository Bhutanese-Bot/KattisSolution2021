serving,paul,opponent = map(int,input().split(' '))
rounds = paul + opponent + 1
rounds += (serving-1)
div = rounds // serving
print("paul") if div % 2!= 0 else print("opponent")
# can implement list seperation for the answer too.