# #methods in list

# #indexing

# marks = [90, 85, 78, 92, 88, 45, 95, 49]
# print(marks[7]) #90
# print(marks) #88
# marks[6] = 98 # 88 ki jagah 98aa jayega
# print(marks) # [90, 85, 78, 92, 88, 45, 98, 49]
# #slicing
# print(marks[2:5]) # [78, 92, 88]
# print(max(marks)) #98
# print(min(marks)) #45
# print(sum(marks)) #645
# print(len(marks)) #8
# print(marks.append(80)) # None
# print(marks.insert(3, 96)) # None
# print(marks.remove(45))
# print(marks.sort()) # None
# marks.sort()
# print(marks.sort())
marks = [90, 85, 78, 92, 88, 45, 95, 49]

marks.sort()    # Pehle list ko sort kar lo (ye line kuch print nahi karegi)
print(marks)    # Ab list ko print karo, ye sorted nazar aayegi
marks.append(80)
print(marks) # Ab 80 list mein nazar aayega
print(sorted(marks)) # Ye sorted list return karta hai
