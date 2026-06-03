name = "Sehar"
friend = "Shazaib"
another_friend = 'Shazaib'

apple1 = "He said,\n\"I want to eat an apple.\""
print(apple1)
apple2 = 'He said, "i want to eat an apple."'
#yaha pr terminal apple ki ak line hi print kry gya q k apple ko numbering nhi di 
#lkn apple ko numbering kr di h tw abi dono print kry ga 
print(apple2)


print("Hellow", name, "and", friend, "and", another_friend)

# Triple quotes se aap poora paragraph likh sakti hain
poem = """Twinkle, twinkle, little star,
How I wonder what you are!
Up above the world so high,
Like a diamond in the sky."""

print(poem)


#yaha pr name variable k character ko access krna sikhty h indexing se
# ab yaha pr indexing ka use krna sikhty h 
#programing mn indexing ki value 0 se start hoti h
print(name[0]) #output will be S
print(name[1]) #output will be e

#ab variable apple ya poem  ki string k sary character ko access krna sikhty h
#yaha pr indexing ka use krna sikhty h or us mn space , next line ka character bhi count hota h


#or us ka tariqa h "for loop"
#loop hun aext ant waly days mn prhy gay 
print("Let use a for loop\n")
for character in poem:
    print(character)
print("Characters in the poem:")



for character in apple2:
    print(character)
print("Characters in the apple2 string:")    
