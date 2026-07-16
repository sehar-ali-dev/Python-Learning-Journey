# =====================================================================
#                PYTHON SET OPERATORS & SIGNS EXERCISE
# =====================================================================
# Python mein Sets par kaam karne ke liye do tareeqe hote hain:
# 1. Built-in Methods (jaise .union(), .intersection())
# 2. Math Operators/Signs (jaise |, &, -, ^)
#
# Neeche sirf un signs aur operators ki list hai jo Python mein use hote hain.
# =====================================================================

# Practice ke liye do basic sets:
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

# ---------------------------------------------------------------------
# 1. Union ( Sign: | )
# ---------------------------------------------------------------------
# Naam: Pipe Operator (Union)
# Kaam: Dono sets ke saare elements ko mila kar ek naya set banata hai.
union_result = A | B 
print("Union (A | B):", union_result)  
# Output: {1, 2, 3, 4, 5, 6}


# ---------------------------------------------------------------------
# 2. Intersection ( Sign: & )
# ---------------------------------------------------------------------
# Naam: Ampersand Operator (Intersection)
# Kaam: Sirf un items ko nikalta hai jo dono sets mein common/same hon.
intersection_result = A & B 
print("Intersection (A & B):", intersection_result)  
# Output: {3, 4}


# ---------------------------------------------------------------------
# 3. Difference ( Sign: - )
# ---------------------------------------------------------------------
# Naam: Minus Operator (Difference)
# Kaam: Pehle set ke wo elements jo doosre set mein maujood nahi hain.
difference_result = A - B 
print("Difference (A - B):", difference_result)  
# Output: {1, 2} (Kyunke 3, 4 set B mein bhi hain)


# ---------------------------------------------------------------------
# 4. Symmetric Difference ( Sign: ^ )
# ---------------------------------------------------------------------
# Naam: Caret Operator (Symmetric Difference)
# Kaam: Wo elements jo dono sets mein common NAHOON (yaani un-common items).
sym_diff_result = A ^ B 
print("Symmetric Difference (A ^ B):", sym_diff_result)  
# Output: {1, 2, 5, 6}


# ---------------------------------------------------------------------
# 5. Subset Check ( Sign: <= )
# ---------------------------------------------------------------------
# Naam: Less than or Equal to (Subset Check)
# Kaam: Check karta hai kya pehle set ke SAARE items doosre set mein hain? (True/False)
small_set = {1, 2}
is_subset = small_set <= A 
print("Subset Check (small_set <= A):", is_subset)  
# Output: True (Kyunke {1, 2} poora ka poora set A mein hai)


# ---------------------------------------------------------------------
# 6. Superset Check ( Sign: >= )
# ---------------------------------------------------------------------
# Naam: Greater than or Equal to (Superset Check)
# Kaam: Check karta hai kya pehle set mein doosre set ke SAARE items maujood hain? (True/False)
is_superset = A >= small_set 
print("Superset Check (A >= small_set):", is_superset)  
# Output: True (Kyunke A bada set hai jo {1, 2} ko apne andar rakhta hai)


# ---------------------------------------------------------------------
# 7. Proper Subset ( Sign: < )
# ---------------------------------------------------------------------
# Naam: Less than (Proper Subset)
# Kaam: Subset check karta hai, lekin dono sets bilkul barabar (equal) nahi hone chahiye.
set_x = {1, 2}
set_y = {1, 2}
print("Proper Subset (set_x < A):", set_x < A)    # Output: True (Kyunke A bada hai)
print("Proper Subset (set_x < set_y):", set_x < set_y) # Output: False (Kyunke dono bilkul barabar hain)


# ---------------------------------------------------------------------
# 8. Proper Superset ( Sign: > )
# ---------------------------------------------------------------------
# Naam: Greater than (Proper Superset)
# Kaam: Superset check karta hai, lekin dono sets bilkul barabar nahi hone chahiye.
print("Proper Superset (A > set_x):", A > set_x)    # Output: True
print("Proper Superset (set_y > set_x):", set_y > set_x) # Output: False


# =====================================================================
# Tip: Is code ko copy kar ke VS Code mein 'set_signs.py' ke naam se save 
# karein aur run kar ke check karein!
# =====================================================================