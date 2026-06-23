# use method in tuple
# tuple ko change krny k liye pehly list mn convert kry gay 
countries = ("spain", "Italy", "India", "England", "Germany")
temp = list(countries)
temp.append("Russia")#add item 
temp.pop(3)#remove item
temp[2] = "Pakistan" #change item
countries = tuple(temp)
print(countries)


#do tuple mil k ak naya typle bnanty h 
countries = ("Turkey", "shrilnka", "Afghanistan", "Iraq")

countries2 = ("Vietnam", "India", "china")
southEastAsia = countries +countries2
print(southEastAsia)
#method of tuple
#count
tuple1 =(0, 1, 2, 3, 2, 3, 1, 3, 2, 3)
res = tuple1.count(3)
print('count of 3 in tuple is:', res)


#index method 
tuple2 =(0, 1, 2, 31, 2, 3, 1, 3, 2, 3)
res = tuple2.index(3)
print('count of 3 in tuple is:', res)

# tuple k specific ki potrtion mn dekhny k liye 
tuple3 =(0, 1, 2, 31, 2, 3, 1, 3, 2, 3)
res = tuple3.index(3, 4, 8)
res = len(tuple3)
print('count of 3 in tuple is:', res)