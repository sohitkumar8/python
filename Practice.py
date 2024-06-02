import random
import time

targetString = "My name is Sohit Kumar and I am a student of BCA"
stringList = "abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ"


i = 0


while i < len(targetString):
    randomChar = random.choice(stringList)
    print(targetString[0:i]+randomChar, end='', flush=True)
    time.sleep(0.01)  # Adding a delay to slow down the print
    print()
    if randomChar == targetString[i]:
        i += 1
     