# Made by TrioHCF#0999

import os, sys, time

os.system('color 3')

print('''
▄▄▄        ▄▄▄▄· ▄• ▄▌▐▄• ▄    ▄▄·  ▄▄▄· ▄▄▌   ▄▄· ▄• ▄▌▄▄▌   ▄▄▄· ▄▄▄▄▄      ▄▄▄  
▀▄ █· ▄█▀▄ ▐█ ▀█▪█▪██▌ █▌█▌▪  ▐█ ▌▪▐█ ▀█ ██•  ▐█ ▌▪█▪██▌██•  ▐█ ▀█ •██   ▄█▀▄ ▀▄ █·
▐▀▀▄ ▐█▌.▐▌▐█▀▀█▄█▌▐█▌ ·██·   ██ ▄▄▄█▀▀█ ██ ▪ ██ ▄▄█▌▐█▌██ ▪ ▄█▀▀█  ▐█.▪▐█▌.▐▌▐▀▀▄ 
▐█•█▌▐█▌.▐▌██▄▪▐█▐█▄█▌▪▐█·█▌  ▐███▌▐█▪ ▐▌▐█▌ ▄▐███▌▐█▄█▌▐█▌ ▄▐█▪ ▐▌ ▐█▌·▐█▌.▐▌▐█•█▌
.▀  ▀ ▀█▄▀▪·▀▀▀▀  ▀▀▀ •▀▀ ▀▀  ·▀▀▀  ▀  ▀ .▀▀▀ ·▀▀▀  ▀▀▀ .▀▀▀  ▀  ▀  ▀▀▀  ▀█▄▀▪.▀  ▀
''')

 
def multiply(x, y):
    return x * y

def subtract(x,y):
    return x - y 

print("[1] B/T Calculator (Calculates the amount you will have inside of the group) - ")
print("[2] Profit Calculator (Calculates the amount of profit you have gained) - ")

choice = int(input("Choice of Calculator: "))

os.system('cls')

if choice == 1:
    print("""Format follows as this: if its 10,000 b/t then enter "10" """)
    num1 = float(input("Enter the amount of b/t: "))
    num2 = 0.7
    os.system('cls')
    print("The format is 1 = 1,000")
    print(num1,"B/T, will get you:", multiply(num1, num2), "A/T")
    time.sleep(30)
    sys.exit

elif choice == 2:
    num1 = float(input("Enter the amount of money you had paid:"))
    num2 = float(input("Enter the amount of money you have gotten: "))
    os.system('cls')
    print("Amount of profit:", subtract(num2, num1))
    time.sleep(30)
    sys.exit()