#strings ko operation k sath kesy use kr skty h

name = "sehar"
#atrings are immutable
#but strings method ka use kr k ak nai strings zaroor bna skty h 

print(len(name))
print(name.upper())# upper case string
print(name.lower())#lower case string

#dicuss "rstrip"
# rstrip name ka chacter h jo remove krta h trailing character ko 
# afe string k agr exclematry ya koi or sign bhi lga ho tw use remove esy' rstrip' sy  krty h
 
name = "sehar !!!!!!!!"
print(name.rstrip("!"))

name = "!!!sehar!!!!!"
print(name.rstrip("!"))# sirf last k sign ko remove krta hai 


#discuss replace()
#replace krta  h dusri string ko 
name = "sehar!!!!sehar"
print(name.replace("sehar", "shazaib"))

#discuss split()
#split string kolist mn convert kr deta hai 
name = "sehar ali" #string mn space ho ga tw hi split ho ga 
print(name.split(" "))


#discuss capitalize()
bolgHeading = "introduCtion to PYthon"
#yaha pr  string mn c or py capital glti se likhy gay h 
#tw capitalize thk kr k likh deta h or string ki heading ka first letter bara kr deta h or baqi sary letter ko lower case mn convert kr deta hai 
print(bolgHeading.capitalize())

# discuss center() method 

str1 = "Welcome to the console!!!!"
print (len(str1))
print(len(str1.center(50)))
#dicuss  endswith() function 
print(str1.endswith("!!!!"))
print(len(str1))
print(str1.endswith("to", 4, 10))#
#discuss find() method
# discuss count() function
# ab ya jana h k name wali strig mn sehar kitni bar a raha h 
print(name.count("sehar"))

#discuss find() method
str2= "He's name is Ali. His an honest man"
print(str2.find("is"))
print(str2.find("ishh"))#output-1


#discus index method 
#print(str2.index("ishh"))#error

#discuss isalnum() function
# string alpha numeric h k nhhi 
#agr punctuation pressnt hon tw false kr deta h 
str3 = "welcomeToTheConsole"
print(str3.isalnum())

str4 ="Welcome"
print(str4.isalpha())#output true
str4 ="Welcome00"
print(str4.isalpha())#output false
#discuss islower() method
print(str4.islower())

#discuss isprintable() method 
str1 = "we wish you Eid Mubarak"
print(str1.isprintable())
#discuss isspace()
str5 = "        "#using tab
print(str5.isspace())#output true

#discuss istitle() method
str6 = "World Health Organization" #title ko capitaliza krny k liye 
print(str6.istitle())
str7 = "To kill a Mocking bird"
print(str7.istitle())
#discuss swapcase() method 
print(str7.swapcase())#ye upper ko lower or lower ko upper caase krta h 

#discuss title() method 
str2= "His name is Ali. Ali an honest man"
print(str2.title())