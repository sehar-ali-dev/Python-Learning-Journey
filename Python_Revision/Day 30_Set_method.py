# =====================================================================
#             PYTHON SETS: ALL SIGNS & METHODS PRACTICE SHEET
# =====================================================================

# ---------------------------------------------------------------------
# 1. UNION (Milaap)
# Sign: |
# Method: .union()
# ---------------------------------------------------------------------
fruits_1 = {"apple", "banana"}
fruits_2 = {"banana", "orange", "mango"}

# A. Sign ke sath:
union_with_sign = fruits_1 | fruits_2
# B. Method ke sath:
union_with_method = fruits_1.union(fruits_2)

print("1. UNION OUTPUTS:")
print("Sign (|) ->", union_with_sign)      # Output: {'apple', 'banana', 'orange', 'mango'}
print("Method  ->", union_with_method)    # Output: {'apple', 'banana', 'orange', 'mango'}
print("-" * 50)


# ---------------------------------------------------------------------
# 2. INTERSECTION (Common elements)
# Sign: &
# Method: .intersection()
# ---------------------------------------------------------------------
lucknow_users = {"Ali", "Sara", "Zain"}
karachi_users = {"Zain", "Raza", "Ali"}

# A. Sign ke sath:
inter_with_sign = lucknow_users & karachi_users
# B. Method ke sath:
inter_with_method = lucknow_users.intersection(karachi_users)

print("2. INTERSECTION OUTPUTS:")
print("Sign (&) ->", inter_with_sign)      # Output: {'Ali', 'Zain'}
print("Method  ->", inter_with_method)    # Output: {'Ali', 'Zain'}
print("-" * 50)


# ---------------------------------------------------------------------
# 3. DIFFERENCE (Pehle set mein ho, doosre mein na ho)
# Sign: -
# Method: .difference()
# ---------------------------------------------------------------------
all_students = {"John", "Emma", "Sam", "Harry"}
present_students = {"Emma", "Harry"}

# A. Sign ke sath:
absent_sign = all_students - present_students
# B. Method ke sath:
absent_method = all_students.difference(present_students)

print("3. DIFFERENCE OUTPUTS (Absent Students):")
print("Sign (-) ->", absent_sign)        # Output: {'John', 'Sam'}
print("Method  ->", absent_method)      # Output: {'John', 'Sam'}
print("-" * 50)


# ---------------------------------------------------------------------
# 4. SYMMETRIC DIFFERENCE (Jo dono mein common NAHOON)
# Sign: ^
# Method: .symmetric_difference()
# ---------------------------------------------------------------------
tea_lovers = {"Asif", "Bilal", "Sana"}
coffee_lovers = {"Sana", "Danial", "Asif"}

# A. Sign ke sath:
exclusive_sign = tea_lovers ^ coffee_lovers
# B. Method ke sath:
exclusive_method = tea_lovers.symmetric_difference(coffee_lovers)

print("4. SYMMETRIC DIFFERENCE OUTPUTS:")
print("Sign (^) ->", exclusive_sign)      # Output: {'Bilal', 'Danial'}
print("Method  ->", exclusive_method)    # Output: {'Bilal', 'Danial'}
print("-" * 50)


# ---------------------------------------------------------------------
# 5. UPDATE METHODS (Asal set ko badal dena)
# Signs: |= (for Union update), &= (for Intersection update)
# Methods: .update() , .intersection_update()
# ---------------------------------------------------------------------
my_skills = {"Python", "HTML"}
new_skills = {"CSS", "JavaScript", "Python"}

# A. .update() (Yaane Union Update: Asal set mein naye items jod dena)
my_skills.update(new_skills)  # my_skills |= new_skills bhi likh sakte hain
print("5. UPDATE OUTPUT:")
print("After .update() ->", my_skills)   # Output: {'Python', 'HTML', 'CSS', 'JavaScript'}

# B. .intersection_update() (Sirf common items ko asal set mein rakhna, baqi delete)
hardware = {"RAM", "CPU", "Mouse"}
input_devices = {"Mouse", "Keyboard"}
hardware.intersection_update(input_devices)
print("After .intersection_update() ->", hardware)  # Output: {'Mouse'}
print("-" * 50)


# ---------------------------------------------------------------------
# 6. DISJOINT CHECK (Kya dono sets bilkul juda/alag hain?)
# No Sign (Sirf method hota hai)
# Method: .isdisjoint() -> True deta hai agar kuch bhi common na ho
# ---------------------------------------------------------------------
veg_food = {"Roti", "Dal"}
non_veg_food = {"Chicken", "Fish"}
mix_food = {"Roti", "Chicken"}

print("6. ISDISJOINT OUTPUTS:")
print("Are Veg and Non-Veg totally different? ->", veg_food.isdisjoint(non_veg_food)) # Output: True (Koi common nahi)
print("Are Veg and Mix totally different?     ->", veg_food.isdisjoint(mix_food))     # Output: False ('Roti' common hai)
print("-" * 50)


# ---------------------------------------------------------------------
# 7. REMOVING ELEMENTS (Set se items delete karna)
# Methods: .remove() , .discard() , .pop() , .clear()
# ---------------------------------------------------------------------
tools = {"VS Code", "GitHub", "Terminal", "Docker"}

# A. .remove() -> Specified item delete karta hai. Agar item na ho to CRASH kar deta hai.
tools.remove("GitHub")
print("7. REMOVE OUTPUT:")
print("After remove('GitHub') ->", tools) # Output: {'VS Code', 'Terminal', 'Docker'}

# B. .discard() -> Safe delete. Agar item set mein na ho, to CRASH NAHI karta.
tools.discard("Not-In-Set") # Kuch nahi hoga, code smooth chalega
tools.discard("Docker")
print("After discard('Docker') ->", tools) # Output: {'VS Code', 'Terminal'}

# C. .pop() -> Randomly (apni marzi se koi bhi) aik element nikalta hai aur return karta hai.
popped_item = tools.pop()
print(f"Popped item -> {popped_item}") 
print("After pop() ->", tools)            # Bacha hua set print hoga

# D. .clear() -> Set ko poora khali kar deta hai.
tools.clear()
print("After clear() ->", tools)          # Output: set() (Khali set)
print("-" * 50)


# ---------------------------------------------------------------------
# 8. SUBSET & SUPERSET (Chota set aur Bada set)
# Signs: <= (Subset), >= (Superset)
# Methods: .issubset() , .issuperset()
# ---------------------------------------------------------------------
parent_bag = {"Notebook", "Pen", "Eraser", "Scale"}
child_bag = {"Pen", "Eraser"}

print("8. SUBSET & SUPERSET OUTPUTS:")
# Kya child_bag ke saare items parent_bag mein hain? (Subset)
print("Is child_bag <= parent_bag?  ->", child_bag <= parent_bag)             # Output: True
print("child_bag.issubset(parent)   ->", child_bag.issubset(parent_bag))       # Output: True

# Kya parent_bag ke paas child_bag ke saare items hain? (Superset)
print("Is parent_bag >= child_bag?  ->", parent_bag >= child_bag)             # Output: True
print("parent.issuperset(child_bag) ->", parent_bag.issuperset(child_bag))     # Output: True
print("=" * 50)