import time
current_time = (time.strftime('%H:%M:%S'))
print("Full time:", current_time )
Hour = int(time.strftime('%H'))
print("Hour:", Hour)
Min = int(time.strftime("%M"))
print("Min:", Min)
Sec = int(time.strftime("%S"))
print("sec:",Sec)


# one method more 
import time

t = time.strftime('%H:%M:%S')

hour = int(time.strftime('%H'))

hour = int(input("Enter hour:" ))

print(hour)

if(hour>=0 and hour<12):

    print("Good Morning Mam")

elif(hour>=12 and hour<17):

    print("Good Afternoon! Mam")

elif(hour>=17 and hour<=23):

    print("Good night Mam")

else:

    print("Have a nice day.")

