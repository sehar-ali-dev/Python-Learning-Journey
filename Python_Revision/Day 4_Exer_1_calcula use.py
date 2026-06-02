# we will use calculator in python 
# firstly we know about arthimetic operators

print(4+8)
print(7-4)
print(4*9)
print(8/2)
print(5%2)
print(5//2)
print(5**2)
print(3**6)


#pracrtice
#create a calculator capaable of peroforming  addition, subtraction, multiplication and division operations on two  numbers. your program ahould format the ooutput in a readable manner.
# get user input for the two numbers and the operation they want to perform 
a = (int(input("enter the first number: ")))
c = (input("enter the operation you want to perform (+, -, *, /, %, //, **): "))
b = (int(input("enter the second number: ")))

print("the sum of a and b is", a+b)
print("the  difference of a and b is",a-b)
print("the product of a and b is",a*b)
print("the division of a and b is",a/b)
print("the modulus of a and b is",a%b)
print("the floor division of a and b is",a//b)
print("the exponentiation of a and b is",a**b)
print("the square of a is",a**2)
