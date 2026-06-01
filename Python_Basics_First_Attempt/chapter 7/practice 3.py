#write a function that takes a string and returns the count of vowels and constants sepratelty
def countVowConso(userinput):
    vowels= "aeiouAEIOU"
    countvowel=0
    countconsonants=0
    for eachChar in userinput:
        if(eachChar.isalpha()):
            if(eachChar in vowels):
                countvowel= countvowel+1
            else:
                 countconsonants+=1

    return countvowel, countconsonants
#fun call
vowels, consonants= countVowConso("Hazrat MOhammad Sawlalahoilhe wasalim")
print (vowels, consonants)

#define a function conert_to_upper(word) that returns the uppercase version of the string

def convert_to_upper(word):
    return word.upper()

print(convert_to_upper("Hazrat MOhammad Sawlalahoilhe wasalim"))

#creat a function full_name(fname, lnmae) that returns the full name hoint with a space
def full_name(fname, lname):
    return (f"{fname} {lname}")
print(full_name("Sehar", "ALI"))






