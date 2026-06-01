#dictionary basic
student= {
    "name": "sehar",
    "city": "Lahore",
    "roll NO": "294807",
    "age": 24,
    "name": "Nalain e fatima",
    "name": "Sahar"
}
# agr dictionary mn ak key do bar likhi tw last wali key print kry ga pehly wali ko ignor kr dy ga 
print(type(student))
print(student["name"])
print(student)
print(student["age"])
print(student["city"])
student["city"]="Karachi"
print(student)
#ak key add krny k liye esy likhy gay 
student["favSubject"]= "Science"
print(student)
#ye dictionary mn sy key ko remove krny k liye 
student.pop("favSubject")
print(student)
print(student.keys())
print(student.fromkeys)
print(student.__doc__)
print(student.values())
