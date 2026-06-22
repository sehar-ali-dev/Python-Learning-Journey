# Learn about tupple
# tupple are not changeable
# tup = (1) ye nt typ aye gi lkn agr tup = (1,) yani comma lgain gay tw tupl bn jie ga 
tup = (1, 5, 6, 4, 87, "sehar", True)
print(type(tup), tup)
print(len(tup))
print(tup[0])
print(tup[1])
print(tup[2])
print(tup[3])

# positive and negative indexing in tupple 
print(tup[-1])
print(tup[-2])

if 87 in tup:
    print("yes 89  is print in tuple.")
else:
    print("false")
# slicing krny k bad ak naya tuple ban jata h 
tup2 = tup[1:4]
print(tup2)