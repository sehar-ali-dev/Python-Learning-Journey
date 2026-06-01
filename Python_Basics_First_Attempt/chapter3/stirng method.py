#string method
str= ("Sehar Ali")
print(str.upper())
print(str.lower())
print(str.title())
print(str.capitalize())
print(str.swapcase())
print(str.count("a"))
print(str.find("a"))
print(str.replace("ali","good"))
#practice question
#take a sentence as input
sentence= input("enter a sentence")
print(sentence.lower())
print(sentence.replace(" ","_"))
print(sentence.upper())
#formated string
print(f"i am sehar ali.i have recently completed my{{bachelors}} in applied psychology from Pak vision college affliated with gcuf{sentence}")
#escape sequences
print("i am sehar ali.\n i have recently completed my bachelors in applied psychology from Pak vision college affliated with gcuf")
print("i am sehar ali.\t i have recently completed my bachelors in applied psychology from Pak vision college affliated with gcuf")
print("i am sehar ali.\b i have recently completed my bachelors in applied psychology from Pak vision college affliated with gcuf")