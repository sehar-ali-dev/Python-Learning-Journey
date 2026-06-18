#File Handling
#mode: "r"- read file, "w"- write, "a"- append 
#"rb/"wb" read and write yani use binary mode
# we work on txt file 

#1st step 
#How to open a file 
#open file
file = open('examplefile.txt', "r")
#read file
file = open('examplefile.txt', "r")
content = file.read()# read all data 
print(content)
file.close()
file = open('examplefile.txt', "r")





file = open('examplefile.txt', "r")
content = file.readline()# read first line   
print(content)
file.close()



file = open('examplefile.txt', "r")
content = file.readlines()# List format mn data dy ga  
print(content)
file.close()

#ab naya data add krna 
#or naya file kesy creat kry gay 4
# "w" agr file exit nhi kr r tw error a jie ga 

file = open('examplefile2.txt', "w")#writemode or file new bni h 
file.write("Assalam O Alaikum!How do you do")# file mn hum yaha sy value likh ry h string mn
#yaha pr overwrite ho ga   
file.close()


#hun ye method use krty h k over write na ho
# append mode 
file = open('examplefile2.txt', "a")
file.write("I am learning python.")
file.close()

#using with statment 
#es sy file khudi pen ho k khudu close ho jaiti h 
with open('examplefile2.txt', 'r')as file:
    content = file.read()
    print(content)

