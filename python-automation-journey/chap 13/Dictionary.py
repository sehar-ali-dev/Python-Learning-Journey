# =====================================================================
# CONCEPT 1: Dictionary Characteristics & Creation
# =====================================================================
# Dictionaries Python 3.7+ se ORDERED hain.
student = {
    "101": "sehar",
    "102": "Aliya",
    "103": "Ali",
    "104": "Shazaib",
    "subject": ["computer", "math", "urdu"]
}

# =====================================================================
# CONCEPT 2: Accessing Elements & Keys/Values Methods
# =====================================================================
student_data = {
    "101": "sehar",
    "102": "Aliya",
    "103": "Ali",
    "104": "Shazaib"
}

# =====================================================================
# CONCEPT 3: Modifying & Updating Data
# =====================================================================
student_data["103"] = "Mena"
student_data.update({"101": "hittler"}) 

# =====================================================================
# CONCEPT 4: Checking Key Existence (Membership Test)
# =====================================================================
if "101" in student_data:
    print("Yes, '101' key exists.")


# =====================================================================
# NEW CONCEPT 5: For Loops in Dictionaries
# =====================================================================
print("\n--- Dictionary Loops Output ---")

# Method 1: Sirf Keys par loop chalana (Default tareeqa)
print("\n1. Printing all keys:")
for key in student_data:
    print(key)

# Method 2: Sirf Values par loop chalana (.values() use kar ke)
print("\n2. Printing all values:")
for val in student_data.values():
    print(val)

# Method 3: Key aur Value dono sath print karna (.items() use kar ke)
# Yeh method industry mein sabse zyada use hota hai!
print("\n3. Printing Key-Value Pairs together:")
for key, value in student_data.items():
    print(f"Roll No: {key} -> Name: {value}")


# =====================================================================
# NEW CONCEPT 6: Removing Elements (pop, popitem, clear, del)
# =====================================================================
print("\n--- Removing Elements Output ---")

# 1. .pop(key) Method: Makhsoos (specific) key ko remove karta hai aur uski value return karta hai
removed_student = student_data.pop("104") # Shazaib ko remove karega
print(f"Removed Student: {removed_student}")
print("Dictionary after .pop():", student_data)

# 2. .popitem() Method: Dictionary ke bilkul aakhri (last inserted) element ko remove karta hai
student_data.popitem() # Jo bhi aakhir mein bacha hoga use nikal dega
print("Dictionary after .popitem():", student_data)

# 3. del keyword: Yeh bhi makhsoos key delete karne ke liye use hota hai
del student_data["102"] # Aliya ko delete karega
print("Dictionary after del keyword:", student_data)

# 4. .clear() Method: Puri dictionary ko khali (empty) kar deta hai, magar dictionary delete nahi hoti
student_data.clear()
print("Dictionary after .clear():", student_data) # Output: {}