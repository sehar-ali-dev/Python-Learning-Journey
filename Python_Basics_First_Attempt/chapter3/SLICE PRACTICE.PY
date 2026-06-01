# write a program that takes your favourite food name as input and prints 
import pprint

#understanding of slicing in python
food= input("enter the food name")
length= len(food)
middle= length//2
print(food)
print(length)
middle_three = food[middle-1 : middle+2]
last_two = food[-2:]
print(last_two)
print("middle 3:", middle_three)
##
# Food name input lena
food = input("Enter your favourite food name: ") # Farz karen user ne 'pineapple' likha

length = len(food)
mid = length // 2

# 1. Middle 3 characters nikalna
# Formula: (mid-1) se (mid+2) tak, taake exact 3 characters aayen
middle_three = food[mid-1 : mid+2]

# 2. Last 2 characters nikalna
# Iske liye hum negative indexing [-2:] use kar sakte hain
last_two = food[-2:]

print("Original Food:", food)
print("Middle 3 characters:", middle_three)
print("Last 2 characters:", last_two)