# string 
#programing k ander sab 0 sy hi start hota hai 

name = "Sehar,Ali,Ghouri"
#mujhe 5 charaters chahiye 6 likhain gay yani ak charater bhrha k likhain gay ta k 5 charater print hon outout mn 
print(name[0:6])


#agr length nikalni h kisi bhi string ki tw  len() function use kry gay 
print(len(name))

fruit = "mango, orange, banana, apple"
print(fruit[0:29])
print(len(fruit)) 

#slicing learn
#slicing k liye [] square braket use krty h 
fruit = "mango"
mangolen = len(fruit)
print(mangolen)
#agr index mn 0 na bhi lgain tw python khud sy lga dy ga 

print(fruit[:6])
print(fruit[0:6])
print(fruit[1:6])
print(fruit[2:6])
print(fruit[3:6])
print(fruit[4:6])

#negative slicing bhi hoti h 
print("negative slice start:")
print(fruit[:6])
print(fruit[0:-3])
print(fruit[-5:-2])
print(fruit[-6:-3])
print(fruit[-5:-3])
print(fruit[0:-3])
print(fruit[0:len(fruit)-3])
#print(fruit[0:len(fruit)-3]) yaha -3 sy pehly python khud len() function use krta h 
#solve quick quiz:
nm = "sehar"
print(nm[-4:-2])









