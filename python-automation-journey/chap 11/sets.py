#set are unordered.
#set are unchangeable
#not allowed in duplicate value
#sets are index
#use in {} bracket
#how to creat set
# different types of data add kr skty h 
#language={1,2,3,True,"ali"}
#use string data 
language={"python","java","c++"}
#if we addet two set any data type 
#language2={"python1","java1","c++1"}
#how to access
#use for loop
#set k element ko access loop k zriye sy kr skty h 
for n in language:
    print(n)

#how to add
language.add("php")
#language.update(language2)

#how to remove
#language.remove("python")
#use also discard method
language.discard("javascript")
#hum pop method bhi use kr skty h
#also use frozen set() es mn na add kr paty h na remove kr paty h


for n in language:
    print(n)



