# Sab se pehle welcome message print hoga
print("Welcome to FizzBuzz!")

def fizzbuzz(num):
    # Agar 3 aur 7 dono se divide ho
    if num % 3 == 0 and num % 7 == 0:
        return "FizzBuzz"
    # Agar sirf 3 se divide ho
    elif num % 3 == 0:
        return "Fizz"
    # Agar sirf 7 se divide ho
    elif num % 7 == 0:
        return "Buzz"
    # --- NAYA TWIST YAHAN LIKHA HAI ---
    elif "3" in str(num):
        return "Almost Fizz"
    else:
        string_num = str(num)
        return string_num

# 1. User se input lena
user_input = int(input())

# 2. 1 se le kar user_input tak loop chalana
for i in range(1, user_input + 1):
    # Har number (i) ka result calculate kar ke sath hi print karna
    print(fizzbuzz(i))