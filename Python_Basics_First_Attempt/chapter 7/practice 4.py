#define a function message (text="keep learning!") and call it with and without an argument.
#function banaya default value k sath
def  message (text="keep learning!"):
    return text
#function ko arguments k sath call kiya 
print(message("pyhon is fun!"))
#function ko bina kisi arguments j (without call kiya)
print(message())

#creat a functio login(username, password="1234") that prints the credentials.
def login(username, password="1234"):
    print(f"username:{username}, password:{password}")
login("ali_99")
login("seharali", "0979")

    

