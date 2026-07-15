# 1. Dictionary Initialize ki
student_records = {}

# 2. Add Student Function
def add_student(name, age, courses):
    if name in student_records:
        print(f"Student '{name}' already exists.")
    else:
        student_records[name] = {
            "age": age,
            "grades": set(),          
            "courses": set(courses)    
        }
        print(f"Student '{name}' added successfully.")

# 3. Add Grade Function
def add_grade(name, grade):
    if name not in student_records:
        print(f"Student '{name}' not found.")
    else:
        student_records[name]["grades"].add(grade)
        print(f"Grade {grade} added for student '{name}'.")

# 4. Is Enrolled Function
def is_enrolled(name, course):
    if name not in student_records:
        print(f"Student '{name}' not found.")
        return False
    if course in student_records[name]["courses"]:
        return True
    else:
        return False

# 5. Calculate Average Grade Function
def calculate_average_grade(name):
    if name not in student_records:
        print(f"Student '{name}' not found.")
        return None
    grades_set = student_records[name]["grades"]
    if len(grades_set) == 0:
        return 0.0
    return float(sum(grades_set) / len(grades_set))

# 6. List Students By Course Function
def list_students_by_course(course):
    enrolled_students = []
    for name, details in student_records.items():
        if course in details["courses"]:
            enrolled_students.append(name)
    return enrolled_students

# 7. NAYA FUNCTION: Filter Top Students
def filter_top_students(threshold):
    top_students = []
    
    # Har student ke naam par loop chalaya
    for name in student_records:
        avg = calculate_average_grade(name)  # Purana function call kiya
        
        # Check kiya ke average threshold se zyada hai ya nahi
        if avg is not None and avg > threshold:
            top_students.append(name)
            
    return top_students

# 8. SAARA TESTING BLOCK SAB SE AAKHIR MEIN:
add_student("Alice", 20, ["Math", "Physics"])
add_student("Bob", 22, ["Math", "Biology"])
add_student("Diana", 23, ["Chemistry", "Physics"])
add_grade("Alice", 90)
add_grade("Alice", 85)
add_grade("Bob", 75)
add_grade("Diana", 95)

print(filter_top_students(80))  # Should return ["Alice", "Diana"]
print(filter_top_students(90))  # Should return ["Diana"]
print(filter_top_students(100)) # Should return []