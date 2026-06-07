subject =input("Enter the email subject:").lower()
email_body=input("Enter the email/comtent:").lower()
# yaha pr two variables ko akhty likhain gay 
#Dono text ko aapas mein jod kar ek bada text bana diya


full_email= subject + " "+ email_body

#Python mein f likh kar quotes lagayein, aur jo variable jahan rakhna hai, use curly brackets {} mein daal dein. Beech mein space bhi aap normal text ki tarah de sakti hain
#full_email = f"{subject} {email_body} {email_address}"

#Agar aapke paas bohot saari cheezein ek list mein hain, toh aap unhein ek hi jhatke mein jod sakti hain
#all_texts = [subject, email_body, email_address]
# full_email = " ".join(all_texts)  # Yeh sab ke beech mein ek ek space laga kar jod dega



if "job"in full_email or "resume" in full_email or "apply" in full_email:
    print("Thank you for applying! Our HR team will review your resume and get back to you soon.")

elif "urgent" in full_email or "emergency" in full_email or "asap" in full_email:
    print("Priority Alert: We have received your urgent request. A team member is looking into it right now!")
elif"refund" in full_email or "money back" in full_email:
    print("Our billing team has been notified. Please allow 3-5 business days to process your refund.")
elif"thanks" in full_email or "thank you" in full_email or "great service" in full_email: 
    print("We are thrilled to hear that! Thank you for your kind words and support.")
else:
    print("Thank you for contacting us. We have received your email and will reply within 24 hours.")