# today we will disciss about variables and data types in python,

a = 10
print(a) # this is a variable and it is storing the value 10
# in python we don't need to declare the data type of a variable, it is dynamically typed
a1 = 20
b = "Sehar Ali"
print(b) # this is a string variable and it is storing the value "Sehar Ali"
c = 3.13*3
print(c) # this is a float variable and it is storing the value 9.39
sehar_ali = "I am 24 years old"
print(sehar_ali) # this is a string variable and it is storing the value "I am 24 years old"
print(a + a1)
d = complex(2, 3)
print(d) # this is a complex variable and it is storing the value (2+3j)
print("this type of a is", type(a))
print("this type of b is", type(b))
print("this type of c is", type(c))
print("this type of sehar_ali is", type(sehar_ali))
print("this type of d is", type(d))
#output
# this type of a is <class 'int'>
# this type of b is <class 'str'>
# this type of c is <class 'float'>
#this type of sehar_ali is <class 'str'>

# boolwan data type means truse or false
e = True
f = False
print(e) # this is a boolean variable and it is storing the value True
print(f) # this is a boolean variable and it is storing the value False
print("this type of e is", type(e))
print("this type of f is", type(f))
# sequenced data type means list, tuple and set
g = ["apple", "mango"] # this is a list variable and it is storing the value ["apple", "mango"]
#variable are mutable means we can change the value of a variable after it has been assigned, but tuple and set are immutable means we cannot change the value of a variable after it has been assigned
h = (1, 2, 3, 4, 5) # this is a tuple variable and it is storing the value (1, 2, 3, 4, 5)
#tuple are immutable means we cannot change the value of a variable after it has been assigned, but list and set are mutable means we can change the value of a variable after it has been assigned
i = {1, 2, 3, 4, 5} # this is a set variable and it is storing the value {1, 2, 3, 4, 5}
#set are mutable means we can change the value of a variable after it has been assigned, but list and tuple are mutable means we can change the value of a variable after it has been assigned
print(g)
print(h)
print(i)
print("this type of g is", type(g))
print("this type of h is", type(h))
print("this type of i is", type(i))

#mapping data type means dictionary
# mean mn key value pair hota h dictionary me, jisme key unique hoti h aur value kisi bhi data type ki ho sakti h
j = {"name": "Sehar Ali", "age": 24} # this is a dictionary variable and it is storing the value {"name": "Sehar Ali", "age": 24}
print(j)
print("this type of j is", type(j))

