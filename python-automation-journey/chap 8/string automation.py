name = '''I am Sehar Ali.I am learning Python.Its very easy.'''
print(name)

name = "I am Sehar Ali.\nI am learning Python.\nIts very easy."
print(name)


#yaha pt index bhi sikh ry h 
# index humesha 0 sy start hota h 
name = "I am Sehar Ali.I am learning Python.Its very easy."

print(len(name))
print(name[0])
print(name[0:23])
print(name[1:14])
print(name[-1])


#sliceing Learnig
name = "I am Sehar Ali.I am learning Python.Its very easy."
print(name.upper())
print(name.lower())#ye automation mn boht use hota h 
print(name.strip())
print(name.find("are"))
print(name.count("a"))
# baz dafa condition lgani prti h 

name = "cilinical Psychologist sehar Ali"
if "Ali" not in name:
    print("Exist")

file_name="Seharali.pdf"
if file_name.endswith("pdf"):#  .startwith() function bhi hota h 
    print("save the file to the pdf folder.")
