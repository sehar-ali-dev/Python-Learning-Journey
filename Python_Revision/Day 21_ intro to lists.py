#list are change able
marks = [3,4,6, "Sehar", True, 6, 7, 2, 32, 345, 23 ]#list mn hum string bhi add kr skty h 
print(marks)
print(type(marks))
print(marks[0])
print(marks[1])
print(marks[2])
print(marks[3])
print(marks[4])
print(marks[len(marks)-3])#negative index
print(marks[5-3])#negative index ko positve mn kiya 
print(marks[2])#positive index


#ab mujhe ye pta krna h k 7 es list mn hai k nhi 
if 7 in marks:
    print("yes")
else:
    print("no")

#same yehi chees hum list ki string mn bhi use krty h 
#same things applies for string as well 
if "Sehar" in marks:
    print("yes")
else:
    print("no")

#yaha marks mujhe sary print krny h 
print(marks)
print(marks[:])
print(marks[1:-1])
print(marks[1:8:2])

#what is List comprehension

lst = [i for i in range(4)]
print(lst)


lst = [i*i for i in range(4) if i%2==0]
print(lst)
