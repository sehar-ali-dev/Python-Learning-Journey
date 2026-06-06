a = int(input("Enter your age"))
print("print your age is:", a)

#conditional operators are <,>,<=,>=,!=, == dbl equal to means equal 
# print(a>18)
# print(a<18)
# print(a<=18)
# print(a>=18)
# print(a==18)
# print(a!=18)# != means is 'not equal to'
if(a > 18):
    print("you can drive.")# es mn jo space a r h esy indentation kehty h 

else:
    print("you can't drive.")


#practice
appleprice = 210
budget = 200
if appleprice <= budget:
    print("sehar, add 1 kg apples to the cart.")
else:
    print("Sehar, do no add apples tho the cart.")


appleprice = 10
budget = 200
if (budget - appleprice > 70 ):
    print("sehar, add 1 kg apples to the cart.")
elif (budget - appleprice > 50):
    print("Its ok you can buy.")
else:
    (print("Sehar, do ot add apples to the cart"))


#example 3 
a = int(input("Enter your age"))
print("print your age is:", a)

#conditional operators are <,>,<=,>=,!=, == dbl equal to means equal 
# print(a>18)
# print(a<18)
# print(a<=18)
# print(a>=18)
# print(a==18)
# print(a!=18)# != means is 'not equal to'
if(a>18):
    print("you can drive.")# es mn jo space a r h esy indentation kehty h 

else:
    print("you can't derive.")


#practice
appleprice = 210
budget = 200
if (appleprice <= budget):
    print("sehar, add 1 kg apples to the cart.")
else:
    print("Sehar, do no add apples tho the cart.")


appleprice = 10
budget = 200
if (budget - appleprice > 50 ):
    print("sehar, add 1 kg apples to the cart.")
elif (budget - appleprice > 70):
    print("Its ok you can buy.")
else:
    (print("Sehar, do ot add apples to the cart19"))


#example 3 
num = int(input("Enter the value of num: "))
if (num < 0):
    print("number is negative.")
elif (num == 0):
    print("number is zero.")
elif (num == 999):
    print("number is special.")
else:
    print("Number is positive")