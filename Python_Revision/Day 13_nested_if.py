# Ek variable banaya aur usmein 19 store kiya
num = int(input("enter the value "))

# 1. Sab se pehle check hoga ki kya number zero se chota (negative) hai?
if (num < 0):
    print("number is negative.")

# 2. Agar number negative nahi hai, toh check hoga ki kya yeh zero se bada (positive) hai?
elif (num > 0):
    # --- Yahan se NESTED (andar wali) conditions shuru hoti hain ---
    
    # Agar number 10 ya us se chota hai (yani 1 se 10 ke darmiyan)
    if (num <= 10):
        print("number is b/w 1-10.")
        
    # Agar number 10 se bada hai AUR 20 ya us se chota hai (yani 11 se 20 ke darmiyan)
    elif (num > 10 and num <= 20):
        print("number is b/w 11-20.")
        
    # Agar number upar wali dono conditions mein nahi aata (yani 20 se bada hai)
    else:
        print("Number is greater than 20")
        
# 3. Agar number na toh negative hai aur na hi positive (yani zero hai)
else:
    print("number is Zero.")