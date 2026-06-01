#writw a code to open a file named mydata.txt in read mode.
# Line 3 ko is tarah se badlein:
file = open("chapter 8/my data.txt", "r", encoding="utf-8")
data = file.read()

print("data of the file is:", data)

#write a program to read a text from a given file certificate.txt and find whether it contains the word live
file = open()
dataoffile= file.read()
dataoffile= dataoffile.lower()
if"live" in dataoffile:
    print("yes live word is present in the file ")
else:
    print("no")

   
