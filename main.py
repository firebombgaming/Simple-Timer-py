import math
import time
import os

i = True

os.system("clear")

timer = float(input("How long do you want a timer for in seconds: "))

while i == True:
    os.system("clear")
    print(timer)
    timer -= 1
    time.sleep(1)
    if timer == 0:
        os.system("clear")
        print("done")
        exit()
