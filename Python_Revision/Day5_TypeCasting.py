# Type Casting in Python
# kisis data tyope ko kisis dusri data type mn convert krna type casting kehlata h
# Type casting is the process of converting one data type to another. In Python, you can use built-in functions to perform type casting.
# Here are some common type casting functions in Python:
a = "1"
b = "2"
# yaha do sting akhty ho k 12 bnaie gay sum krny sy 3 nhi aye ga 
print(a+b)#output will be 12 because both a and b are strings

#ak ye pattern h sting ko int mn convert krny ka 
# to convert string to integer
a = int("1")
b = int("2")
print(a+b)#output will be 3 because both a and b are integers

#ak ye patteren h 
a = 1
b = 2
print(a+b)

#two type of typecasting
#1: Explicit Conversion 
#2: Implicit Conversion

#implicit type casting
d = 3.5
e = 6
print(d+e) #output will be <class 'float'>
print(type(d+e)) #output will be 9.5 because d is a float and e is an integer, so e is implicitly converted to a float before the addition

