#rule based AI chatbot

import datetime
import time

name= input("welcome, enter your name:")
presentHour =datetime.datetime.now().hour
if 5 <= presentHour <= 11:
    print("good morning,",name)
elif 11 <= presentHour <= 17:
    print("good afternoon,",name)
elif 17<= presentHour <= 20:
    print("good evening,",name)
else:
    print("good night,",name)

print("welcome to your buddy chatbot ")
print("you can ask me basic question, type, 'buy' to exit from the bo\n")
# chatot ki memory creation [dictionary of responces]

responses = {"hellow": "Hi, welcome. How can i help you?",
             "how are you": "I am ver fine. thank you.",
             "who are you": "I am very smart ai chatbor",
             "motivated me": "stay postive and keep going every bug of your project makes you a better developer best",
             "happy": "grat to hear that",
            "function kiya hoty hai": "ja kr chapter 7 mn prho",
            "sad": "don't worry cheers up! Every thing will be fine",
            "Tell me about python": "python is an amazing and easy language.",
            "Tell me about weather": "I can't check live weather, but i hope it's pleasent!"
              }

#methof/function to get responsse of chatbot
def getresponseofbot(userQuestion):
    userQuestion= userQuestion.lower()
    for eachkey in responses:
        if eachkey in userQuestion:
            return responses[eachkey]
        
    return "I am not able to tell that yet. I am still in learning mode"



#take user input

while True:
    userinput = input("\nplease ask your question: ")  # Message theek kiya
    
    # Agar user 'bye' kahe toh foran band ho jaye
    if "bye" in userinput.lower():
        print("Bot response: Goodbye! Have a great day!")
        break
        
    reply = getresponseofbot(userinput)
    
    # <--- YAHAN 1 SECOND KA DELAY LAGAYA --->
    time.sleep(2)
    
    print("bot response:", reply)  # Ab yeh sirf EK hi baar print karega

#Add at least 3 new question and responses to the chatbot
#add logic to reponses differently if the user say "sad" or "happy".
#Add a delay(1 second) b/w question and answer user time.sleep()