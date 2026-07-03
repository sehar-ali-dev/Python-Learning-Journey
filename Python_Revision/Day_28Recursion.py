# functoin k ander hum function run kr skty h 
# like agr average function k ander sum function run kr skty h
#  factotial (7)= 7*6*5*4*3*2*1
# factorial  (5)= 5*4*3*2*1
# by defination fatorial  jo ) hota h us ki default value 1 h 
# facrorial(n)= n*factorail(n-1) __ formula 
# formula use kr k recursion k ander function ko call krty h mtln ab ye sikhna h 
def factorial(n):
    if(n==0 or n==1):
        return 1
    else:
        return n * factorial(n-1)  # recursion k ander function ko call krty h
print(factorial(3))  
print(factorial(4))    
print("factorial of 5 is:", factorial(5))# 5*4*3*2*1=120