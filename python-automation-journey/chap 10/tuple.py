# ==========================================
# 1. TUPLE KI BASIC INFORMATION & CREATION
# ==========================================

# RULE: Agar tuple mein sirf EK value likhni ho, toh comma lgana zaroori hai.
# Comma hamesha quotation marks ke BAHAR aana chahiye, aise:
student2 = ("Aliya",) 

# CONCEPT: Tuples are "ordered" (inkay items ka ek fix order hota hai).
# CONCEPT: Tuples are "unchangeable" (bannay ke baad inhein badla nahi ja sakta).
# CONCEPT: Tuples mein data duplicate bhi ho sakta hai (jaise neeche 'Sehar' do baar hai).
# CONCEPT: We can add multiple types of data (int, float, string, boolean sab chal sakta hai).
student = ("sehar", "Ali", "Khan", "Sehar", "Hittler")
print("Original Tuple:", student)


# ==========================================
# 2. PACKING AND UNPACKING CONCEPT
# ==========================================

# Unpacking tabhi chalegi jab 'student' tuple pehle se bana hua ho.
# Yaad rahe: Jitne items tuple mein hain (5 items), utne hi variables hone chahiye!
(s1, s2, s3, s4, s5) = student 
print("Unpacking Test (s1):", s1) # Yeh 'sehar' print karega


# ==========================================
# 3. HOW TO ACCESS ITEMS (INDEXING & CONDITIONS)
# ==========================================

# Index use kar ke access karna (Slicing):
print("Sliced Tuple [0:5]:", student[0:5])

# Condition use kar ke check karna:
if "Hittler" in student:
    print("Yes, Hittler is in the tuple.")


# ==========================================
# 4. HOW TO UPDATE A TUPLE (THE TRICK)
# ==========================================

# Pehle tuple ko list mein convert karenge:
Student_list = list(student)

# Method 1: Index use kar ke change karna
Student_list[0] = "Shazaib"

# SAWAL: "Hum index ke ilawa bhi koi method use kar sakte hain?"
# JAWAB: Ji han! Chunkay yeh ab LIST ban chuki hai, toh aap list ke methods use kar sakti hain:
Student_list.append("Zain")       # Akhir mein naya naam jorhne ke liye
Student_list.remove("Ali")        # Kisi khaas naam ko delete karne ke liye
Student_list.insert(1, "Ayesha")  # Kisi specific jagah par naya naam dalne ke liye

# Ab dubarah list ko tuple mein change kar denge:
student = tuple(Student_list)
print("Updated Tuple (After List conversion):", student)


# ==========================================
# 5. JOINING TWO TUPLES (ADDITION)
# ==========================================

# Ab yahan par 2 tuples ko add kar rahe hain (student aur upar banaya hua student2)
student += student2
#use for loop
for n in student:
    print(n)
#while loop
i=0
while i<len(student):
    print(student[i])
    i=i+1
print("Final Tuple after adding student2:", student)

#Aapko har dafa index [0] likhne ki zaroorat nahi. Aap .append(), .remove(), ya .insert() use kar ke poori list badal sakti hain, aur phir wapis use tuple() mein convert kar dein!