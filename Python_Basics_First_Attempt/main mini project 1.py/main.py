# expense tracer projecr

expenseslist = []
 #list of all expenses in form of dictionary
print("welcome to expense tracker : khrcha kam kiya kro ")

while True:
    print("====MENU====")
    print("1. ADD Expense")
    print("2. View all Expenses")
    print("3. view total kharcha")
    print("4.Exit")

    choice= int(input("please enter your choice:"))

# add expense
    if(choice == 1):
        date= input("kis date pr kharcha kiya tha?")
        category= input("kis type ka kharcha kiya (food, travel, makeup)")
        description= input("aur detail dedo")
        amount= float(input("enter the  amount:"))

        expense= {
            "date": date,
            "category": category,
            "description": description,
            "amount": amount
        }      

        expenseslist.append(expense)
        print("\n Done bro. Expense is added is successfully")   
# 2. view all expenses                

    elif(choice == 2):
        if (len(expenseslist)==0):
            print("No Expenses Added. jao pehly paisy khrch kro ")
        else:
            print("===== ye ap ka sara exppense =====") 
            count= 1
            for eachkharcha in expenseslist:
                print(f"kharcha number {count}-> {eachkharcha["date"]}, {eachkharcha["category"]}, {eachkharcha["description"]}, {eachkharcha["amount"]}")
                count= count+1
# 3. view total spending"
    elif(choice ==3):
        total=0
        for eachkharcha in expenseslist:
            total = total + eachkharcha["amount"]
        print("\n total kharcha = ", total)
#4 exit
    elif(choice == 4):
        print("thank you ap ny humara system use kiya ")
        break

    else:
        print("INVALID CHOICE.TAR AGAIN")

            

         