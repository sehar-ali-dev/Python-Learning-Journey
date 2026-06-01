# write a program using for and range tp print all even numbers between 1 and 20
# range(start, step, stop)
# for item in range(2, 20, 2):
#     print(item)

# # practice 9
# # write a program  to print numbers from 1 to 50 , but print "sehar ali" instead of numbers that are multiples of 5.
n= 1
while n <= 50:
    if n % 5 == 0:
        print("sehar ali")
    else:
        print(n)
    n = n + 1

# practtice 10
# write a program to prrint the  square of each numbers from 1 to 10 using a for loop
for i in range(1, 11):
    square = i ** 2
    print(f"{i} ka square {square} hai")
# write a program that prints the multiplication table of any number entered by the user using a for loop
for i in range(1, 11):
    result = n * i
    print("{} x {} = {}".format(n, i, result))
# copy
for i in range(1, 11):
    result = 3 * i
    print("{} x {} = {}".format(3, i, result))

