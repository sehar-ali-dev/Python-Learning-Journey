class student:
    school_name= "ABC school"
    def __init__(self, name, course):
        # print ("whenever a new object is created i am called automatically")
        # print(self)
        self.name= name
        self.course= course
student1= student("khushi", "Btech")#init method will be called
print("student1 Name:", student1.name)
print("student1 Course:", student1.course)      

student2= student("Ankit", "Bsc")
print("student2 Name-", student2.name)
print("student2 Course-", student2.course)      




        # print("whenever a new object is created I am called automatically")



# Student1= student() #init method will be called
# student2= student()

