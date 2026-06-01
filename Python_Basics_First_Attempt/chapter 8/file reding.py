# #'with' keyword h jo file ko automatically close kr deta hai
# # phir file.close likhny ki zaroort nhi pry gi 

# file = open("chapter 8/report.txt", "r")
# data= file.read()
# file.close()
# #  read entire file
# # ab with sy file ko open kry gay 
# with open("chapter 8/report.txt", "r") as f:
# # 'f' ki jga kuch bhi alphabat likh skty h q k f funstion perform kr raha h 
#     # ab f k uper kuch bhi operation perform kr skty h 
#     data= f.read()
#     print("file data",data)
with open("chapter 8/newTEXTfile.txt", "r") as  f:
#     line1= f.readline()
#     line2= f.readline()
#     line3= f.readline()
#     line4= f.readline()
#     line5= f.readline()
#     line6= f.readline()
#     data= f.read()
#     print("Line 1",line1)
#     print("Line 2",line2)
#     print("Line 3",line3)
#     print("Line 4",line4)
#     print("Line 5",line5)
#     print("Line 6",line6)
#     print("file data", data)
    readlinesMethod= f. readlines()
    print(readlinesMethod)