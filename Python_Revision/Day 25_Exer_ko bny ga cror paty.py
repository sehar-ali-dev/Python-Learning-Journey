# creat a program capable of displaying questions to the user like KBC
#  use list data type to store questions and their correct answer
# display the final amount the person is taking home after playing game


# Questions, Options aur Answers ki alag lists
questions = [
    "Pakistan ka darul hukumat (capital) kaun sa hai?",
    "Python mein text save karne ke liye kaun si data type use hoti hai?"
]

options = [
    ["A) Karachi", "B) Lahore", "C) Islamabad", "D) Peshawar"],
    ["A) int", "B) str", "C) float", "D) boolean"]
]

answers = ["C", "B"]
prize_money = [1000, 5000] # Har sawal ki raqam

total_won = 0

# Loop ke zariye ek ek karke sawal poochna
for i in range(len(questions)):
    print(f"\nSawal {i+1} ({prize_money[i]} Rupay ke liye):")
    print(questions[i])
    
    # Options dikhana
    for option in options[i]:
        print(option)
        
    user_answer = input("Apna jawab likhein (A, B, C, D): ").upper()
    
    if user_answer == answers[i]:
        print("💥 BILKUL SAHI JAWAB! Aap jeet gaye hain!")
        total_won = prize_money[i]
    else:
        print("❌ Afsos! Galt jawab. Game yahin khatam hota hai.")
        break # Galt jawab par game khatam

print(f"\n🎉 Aap ghar lekar ja rahe hain: {total_won} Rupay!")