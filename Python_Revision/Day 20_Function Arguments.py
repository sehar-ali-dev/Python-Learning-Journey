# ==========================================
# FUNCTIONS & ARGUMENTS IN PYTHON
# ==========================================

# ------------------------------------------
# 1. Required Arguments
# ------------------------------------------
# Required arguments wo hote hain jo function
# call karte waqt dena zaroori hota hai.

def average(a, b):
    print("The average is:", (a + b) / 2)

average(4, 6)
average(9, 3)


# ------------------------------------------
# 2. Default Arguments
# ------------------------------------------
# Default arguments ki pehle se value hoti hai.
# Agar value na dein to default value use hoti hai.

def average(a=7, b=4):
    print("The average is:", (a + b) / 2)

average()          # a=7, b=4
average(6, 3)      # a=6, b=3
average(5)         # a=5, b=4 (default)
average(b=8)       # a=7 (default), b=8


# ------------------------------------------
# 3. Keyword Arguments
# ------------------------------------------
# Is mein arguments ka order change kar sakte hain.

average(b=3, a=4)


# Example

def name(fname, mname="John", lname="Watson"):
    print("Hello,", fname, mname, lname)

name("Amy")
name("Ali", "Ahmed", "Khan")
name(fname="Sara", lname="Malik")


# ------------------------------------------
# 4. Variable Length Arguments
# ------------------------------------------
# Jab arguments ki quantity pehle se na pata ho
# to *args use karte hain.

def average(*numbers):#(*numbers) es likhny sy tuple bn jata h 

    total = 0

    for i in numbers:
        total += i

    print("Average is:", total / len(numbers))

average(5, 10, 15)
average(2, 4, 6, 8, 10)
average(1, 2, 3, 4, 5, 6)


# **name multiple keyword arguments ko
# dictionary ki form mein receive karta hai.

def name(**name):

    # Dictionary se values key ke through access kar rahe hain
    print(
        "Hello,",
        name["fname"],   # fname ki value
        name["mname"],   # mname ki value
        name["lname"]    # lname ki value
    )

# Function call
# Order matter nahi karta kyun ke ye keyword arguments hain
name(
    mname="Buchanan",
    lname="Barnes",
    fname="James"
)