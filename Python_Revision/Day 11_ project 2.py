#"Psychology Quiz App" (Score Tracker).
print("=====Welcome to the Stress-O-Meter Quiz=====")
print("give answers only yes or no\n")

score =0
ans1=(input("Kya aap ko aaj kal choti choti baaton par gussa aata hai?").lower())
if ans1 == "yes":
    score = score + 1
ans2=(input("Kya aap ko raat ko neend aane mein mushkil hoti hai?"))
if ans2 == "yes":
    score = score + 1
ans3=(input("Kya aap ko kaam ke waqt focus karne mein masla hota hai?"))
if ans3 == "yes":
    score = score + 1
print("\n----AP KA RESULT----")
print("Ap ka total stress score hai:", score, "out of 3")
if score >= 2:
    print("Mashwara: Aap ko thoda relax karne aur break lene ki zaroorat hai.")
else:
    print("Boht achay! Aap ka stress level control mein lag raha hai.")