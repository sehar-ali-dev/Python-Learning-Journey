# Number even ya odd.
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("even")
else:
    print("Odd")

#TAsk 2
age = int(input("Enter the age: "))
if age >18:
    print("Eligible")
else:
    print("Not Eligible")

#TAsk 3
num1 = int(input("Enter the 1st number"))
num2 = int(input("Enter the 2nd number"))
num3 = int(input("Enter the 3rd number"))

largest = num1
if num2 > largest:
    largest = num2
if num2 > largest:
    largest = num3
print("Largest number is:", largest)

# Dono checks independent (alag alag) hain.

# Pehle num2 check hota hai
# Phir num3 check hota hai
# Dono ka result ek dusre par depend nahi karta

# Is liye 2 separate if statements use kiye gaye hain.

# 2nd method

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

if num1 >= num2 and num1 >= num3:
    print("Largest number is:", num1)

elif num2 >= num1 and num2 >= num3:
    print("Largest number is:", num2)

else:
    print("Largest number is:", num3)
