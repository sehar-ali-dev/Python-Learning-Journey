#write a program with a local verable score inside a funnction and a gllobal one outside

score = 100
def my_fun():
    score = 25
    print(f"fun k andar walal (local) score: {score}")
my_fun()
print(f"fun k bahar wala (global) score:{score}")

#creat a program using global keyword to modify a veriable from inside a function
counter = 10
def my_counter():
    global counter
    counter = counter + 5
    print(f"function k ander k counter ki bdli value:{counter}")

print(f"Function chalne sy pehly global counter:{counter}")   
my_counter()
print(f"Function chalne ke BAAD global counter:{counter}")