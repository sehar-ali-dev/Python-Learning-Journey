# Project: Secret Message Encoder
# Concept: String Slicing & Concatenation

message = input("Apna secret message likhein: ")

# Step 1: Agar message 3 characters se bada hai
if len(message) >= 3:
    # 1. Pehla character uthao
    first_char = message[0]
    
    # 2. Baqi characters (index 1 se aakhir tak) slice karo
    remaining_part = message[1:]
    
    # 3. Naya word banayein: Baqi hissa + Pehla char + Random alphabet
    secret_code = remaining_part + first_char + "xy"
    
    print("Aap ka encoded message hai:", secret_code)

else:
    # Agar word chota hai toh bas use ulta (reverse) kar do
    print("Chota message hai, reverse output:", message[::-1])