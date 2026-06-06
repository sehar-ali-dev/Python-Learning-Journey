#Match case feature is important for interview
x = int(input("Enter the value of x: 90"))
# x is a variable to match x:
match x:
    #if x is 0
    case 0:print("x is zero")
    #case with if-condition
    case 4:
        print("case is 4")
    #empty case with if-condition
    case _ if x!=90:
        print(x, "is not 90")
    case _ if x!=80:
        print(x, "is not 80")
    case _:
        print(x)

    #default case(will only be matched if the above cases were not matched)
    #so it is basically just an els:
    # default k liye under score use hota hai 
    






#example 2 
day = "Saturday"

match day:
    case "Monday":
        print("Oh ho! Aaj toh kaam ka pehla din hai.")
    case "Friday":
        print("Jumma Mubarak! Weekend shuru hone wala hai.")
    case "Saturday" | "Sunday":  # Yahan '|' ka matlab hai 'OR' (ya)
        print("Yeehaa! Aaj toh chutti ka din hai!")
    case _:  # Yeh underscore '_' else ki tarah kaam karta hai (Default case)
        print("Yeh koi aam sa normal din hai.")
#in case mn if-elif-else bhi use krty hai




#break statment  learn



