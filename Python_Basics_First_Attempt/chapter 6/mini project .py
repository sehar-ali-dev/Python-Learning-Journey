# project name: countdown timer (with 1 secong gap)
# print a countdown  before something "exciting" happens (like "laumching..." or "happy new year")
from calendar import c
import time


for i in range(10, 1, -1):
    print(i)
    time.sleep(1)
    print("launching.....!")

import time # Thoda gap dene ke liye (optional)

# range(start, stop, step)
# Start 10 se, Stop 0 par (taaki 1 tak chale), aur -1 ka step (ulta chalne ke liye)
for i in range(10, 0, -1):
    print(i)
    time.sleep(1) # Har number ke baad 1 second ka intezar

print("🚀 Launching...!\nHAPPY NEW YEAR")