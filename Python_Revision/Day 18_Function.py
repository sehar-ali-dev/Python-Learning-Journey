# 1. Pehle hum apne saare functions define kar lete hain
def mean(a, b):
    result = (a * b) / (a + b)
    print(f"The result is: {result}")

def isgreater(a, b):
    if a > b:
        print("First number is greater.")
    else:
        print("Second number is greater or equal.")

# --- AB CODE EXECUTE HONA SHURU HOGA ---

# Pehla hissa: mean function ko test karna (float ke sath)
num1 = float(input("Enter the value a: "))
num2 = float(input("Enter the value b: "))
mean(num1, num2)

print("-" * 20) # Alag karne ke liye line

# Dusra hissa: mean function ko integer ke sath test karna
num3 = int(input("Enter the value a: "))
num4 = int(input("Enter the value b: "))
mean(num3, num4)

print("-" * 20)

# Tisra hissa: isgreater function ko chalana
num5 = int(input("Enter the value a for comparison: "))
num6 = int(input("Enter the value b for comparison: "))
isgreater(num5, num6) # Yeh check karega kaunsa bara hai

# Agar aap inhi do numbers ka mean bhi nikalna chahte hain:
mean(num5, num6)