#ask the user for their 3 favorite movies and them in a list.
# creat a tuple of marks (87, 64, 33, 95, 76)
#write a program to check grade based on marks(A/B/C/D) uning if-elif-else.
# movies = []
# mi = (input("enter the 1st movie:"))
# m2 = (input("enter the 2nd movie:"))
# m3 = (input("enter the 3rd movie:"))
# movies.append(mi)
# movies.append(m2)
# movies.append(m3)
# print(movies)
# print(("my favorite movies are:", movies))
# print("Your favorite movies are:", movies)
#marks ka tupe banana
# marks = (87,64,33, 95, 76)
# print(marks)
# print(type(marks))
#user sy marks lena
# score = int(input("90, 80,70,60"))
# if score>=90:
#     grade="A"
# elif score>=80:
#     grade="B"
# elif score>=70:
#     grade="C"
# elif score>=60:
#     grade="D"
# else:
#     grade="F (fail)"
#     print("grade")

 # User se kafi saare marks mangna (comma ke sath)
user_input = input("Enter marks separated by comma (e.g. 90, 80, 45): ")

# Marks ko alag alag karke list mein dalna
marks_list = user_input.split(",")

for m in marks_list:
    score = int(m.strip()) # strip() faltu spaces khatam kar dega
    
    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    elif score >= 60:
        grade = "D"
    else:
        grade = "F"
    
    