import os
# current working directory print karo
print(os.getcwd())
# current folder ki tamam files aur folders dikhao
print(os.listdir())
# check karo file exist karti hai ya nahi
print(os.path.exists("main.py"))
# folder aur file ko safely join karo
path = os.path.join("Documents", "notes.txt")

print(path)

# file name aur extension alag karo
name, ext = os.path.splitext("report.pdf")

print(name)
print(ext)

# folder create karo
#os.mkdir("practice_folder")

#print("Folder created")

# folder delete karo
os.rmdir("practice_folder")

print("Folder deleted")