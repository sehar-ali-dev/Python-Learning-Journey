saved_password = "python123"
security_answer = "blue"
#system ko lgatar chalany k liye whileloop lgaya h 
while True:
    print("\n---Welcome to the sceure system")
    print("1. Login")
    print("2. Forget Password")
    print("3. Exit Program (System Bnd Krain)")

    choice=input("Select the option(1,2 and 3):").strip()
# Python ka modern Match-Case system
    match choice:
        case "1":
            password=input("Enter your Password: ").strip()
            if password == saved_password:
                print("🔓 Access Granted! Entering the app...")
                break# Sahi login par loop khatam ho jayega aur user andar chala jayega
            elif password == "":
                print("⚠️ Please enter a password.")
            else:
                print("❌ Wrong Password.")
        case "2":
            print("\n---Password Recovery---")  
            answer= input("What is your favorite color?").strip().lower()
            if answer== security_answer:   
                new_password = input("Security verified! Enter your NEW password: ").strip()
                if new_password!="":
                    saved_password = new_password# Password update ho gaya
                    print("✅ Password changed successfully!")
                    print("🔄 Returning to main menu so you can login with your new password...")
                    # Yahan break NAHI lagaya, taake loop dobara chale aur user login kar sake
                else:
                    print("⚠️ Password cannot be empty!")
            else:
                print("❌ Incorrect security answer. Access Denied!")
        case "3":
            print("👋 System shutting down. Goodbye!")
            break # Loop khatam aur program band
        case _:
            # Yeh 'case _' bilkul 'else' ki tarah kaam karta hai (Default case)
            print("⚠️ Invalid option selected. Please choose 1, 2, or 3.")



    
