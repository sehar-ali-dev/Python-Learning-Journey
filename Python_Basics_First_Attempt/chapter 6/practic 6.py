# sehar wants to print her name 5 time, but each time with a number in front of it. write a program using a whil loop that prints:
n=(int(input("enter the number")))
name=1
while name <= n:
    print(name, "sehar ali")
    name = name + 1
# second method
# User se number input lena (aapke case mein 5)
n = int(input("Enter the number of times to print: "))

# Counter shuru karte hain 1 se
name = 1

# While loop jo tab tak chalay ga jab tak i, n se chota ya barabar hai
while name <= n:
    print(name, "Sehar")
    name = name + 1  # Har baar i mein 1 ka izafa (increment) karein