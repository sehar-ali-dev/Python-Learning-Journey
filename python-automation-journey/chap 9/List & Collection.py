#list
# ak variable mn multiples values store kr skty h 
# 3 important things about list 
#List mn  elements change kr skty h 
#List mn duplicate element add kr skty h 
#list ordered hoti h 
# 1st method list ko creat krny ka 
Languages=["python","Java","C++","Html"]
#2nd method list ko creat krny ka 
language2=list(("Html", "Java script", "C++", "python"))
# ye dono list k ander strings h
#ab hum list ko int mn bhi likh skty h 
#number=[1,2,3,4,5,4,5,6,6,7,] also called list
#ab es mn List mn different data types bhi likh skty h 

#numbers=["python",123,True] also called list

print(Languages[1:])
#es method sy naya element add kr skty h list mn 
#but insert ki help sy hum element ko kahin bhi list k order mn add kr skty h
Languages.insert(3,"Go")
print(Languages)

#append() sy bhi list mn element add kr skty h 
Languages.append("Css")
print(Languages)

# .extend() method

#Languages.extend(language2)
print(Languages)

#.remove method
#Languages.remove("C++") #C++ remove ho gaya h list sy 

#pop method
#Pop() akhri element ko remove kr dy ga list mn sy 
#Languages.pop()#pon method mn value bhi add kr k list mn sy remove kr skty h 

# del method 
#ye  del method puri list  ko bhi remove kr ska h  
#or list mn data ko bhi remove kr k error show kr skta h 
#del Languages[2] # index ko pass kr do 

#clear() method 
#ye sirf data ko remove krta h list baqi rhy gi 
Languages.clear()
print(Languages)

