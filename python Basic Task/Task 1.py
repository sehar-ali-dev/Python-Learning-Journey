#task Variables & Input

print("====User Profile====".upper().center(30))

first_name=input("Enter your  name: ").strip().lower()

age=int(input("Enter you age: "))

city=input("Enter your city: ").strip().lower()

print(f"Name: {first_name}")
print(f"Age: {age}")
print(f"City: {city}")
print("--------------".center(30))

#second method
print("====User Profile====".upper())
Name = ("Sehar")
last_name=("Ali")
age = 24
city = ("Lahore")
print(f"Name: {Name}{last_name}\nAge: {age}\nCity:{city}")
print("----------.center(30)")

#User se age lo aur batao 5 saal baad kitni hogi.
Age = int(input("Enter the age: "))
print("Age after 5 year:", Age + 5)

#User se city aur country lo aur ek sentence print karo

city =input("enter the city: ")
country =input("enter the country: ")
print(city,"is a beautiful city of",country + ".")