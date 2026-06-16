#Data Types
# 2 numbers lo aur:

# Sum
# Difference
# Multiplication
# Division

# print karo.


x = int(input("enter the value of x: "))
y= int(input("enter the value of y: "))
total = x+y
diff = x-y
multiply = x*y
Divided = x/y

print(f"Total: {total}\ndifference: {diff}\nmultiply: {multiply}\nDivided: {Divided}")

# User ka weight lo aur uska data type print karo.
weight =float(input("enter the weight: "))
print(type(weight))

#Strings
name =("sehar Ali")
print(name.upper())
print(len(name))

sentence = (input("Enter the sentence: "))
count_a = (sentence.count("a"))
print("Number of 'a' in sentence:",count_a)