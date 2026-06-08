print("welcome to personal expense tracker")
food = 0.0
transport = 0.0
bills = 0.0
shopping = 0.0
tours = 0.0
other = 0.0



while True:
    

    print("\nchoose an option")
    print("Add Expense")
    print("Show Summary")
    print("Data Export")
    print("exit")
    

    choice= input("\nEnter your choice : ")

    match choice:
        case "1":
            print("\nCategory: Food, Transport, Shopping, Tours, Bill, other")
            category = input("enter category: ").lower()
            amount = float(input("Enter amount: "))
            if category=="food":
                food +=amount
            elif category=="transport":
                transport +=amount
            elif category=="Shopping":
                shopping +=amount
            elif category=="Tours":
                tours +=amount
            elif category=="bills":
                bill +=amount
            else:
                other +=amount
            total = food + transport + shopping + tours + bills + other
            print(f"Added $ {amount} to {category} category")
            print(f"Current Total Expense: $ {total}")

        case "2":
            print("show summary")
            print("\n--- Expense Summary ---")
            print(f"Food: $ {food}")
            print(f"Transport: $ {transport}")
            print(f"Shopping: $ {shopping}")
            print(f"Tours: $ {tours}")
            print(f"Bills: $ {bills}")
            print(f"Other: $ {other}")
            total = food + transport + shopping + tours + bills + other
            print(f"Total Spent: $ {total}")
            
            if total>500:
                print("warning! You have spent more than 500 in this month.")
            elif total==0:
                print("your have not added any expense yet.")
            else:
                print("your managing your budget wisely. ")

        case "3":
            print("Data Export")#es ko hum esy hi chor dy gay jb file handling wala chapter kry gay us mn kry gay 
        case "4":
            print("exit")#case 3 and case 4 ko dono ko bad mn kry gay 
            break
        case _:
            print("invalid input")