import os
from time import sleep
import smtplib
import platform

red = '\033[31m'
reset = '\033[0m'
green = '\033[32m'
yellow = '\033[33m'
blue = '\033[34m'
#orange = '\033[033m'
P = '\033[15m'  # purple
orange = '\033[38;5;208m'
magenta = '\033[35m'
cyan = '\033[36m'

def CheckOS():
    OS = platform.system()
    if OS == "Windows":
        print(" + --------------------------------- +")
        print(f"+ Detected Operation System : ", OS, "+")
        print(" + Linux is better than Windows      +")
        print(" + --------------------------------- +")
        sleep(2)
    elif OS == "Linux":
        print(" + --------------------------------- +")
        print(f"+ Detected Operation System : ", OS, "+")
        print(" + Is perfect to control Linux OS    +")
        print(" + --------------------------------- +")
        sleep(2)
    else:
        print("+ -------------------------------------- +")
        print(f"{red}+ Unknown Operation System{reset}")
        print("+ -------------------------------------- +")
        sleep(2)
CheckOS()

def MailLogo():
    os.system("clear")
    sleep(0.3)
    print("\n")
    print("\n")
    print(f"@@@@@&##&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&##&@@@@@")
    print(f"@@@@@&##&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&##&@@@@@")
    print(f"@@@{red}@&#&@@@{reset}@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@{red}@@&#&@{reset}@@@")
    print(f"@@@{red}&##@@@@{blue}&#&&{reset}@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@{blue}&&#&{reset}{red}@@@@##&{reset}@@@{reset}")
    print(f"@@@{red}&##@@@@@{blue}&&##&{reset}@@@@@@@@@@@@@@@@@@@@@@@@@@@@{blue}&##&&{reset}{red}@@@@@##&{reset}@@@{reset}")
    print(f"@@@{red}&##@@@@@@@{blue}&&##&{reset}@@@@@@@@@@@@@@@@@@@@@@@@{blue}&##&&{reset}{red}@@@@@@@##&{reset}@@@{reset}")
    print(f"@@@{red}&##@@@@@@@@@@{blue}&##&{reset}@@@@@@@@@@@@@@@@@@@@{blue}&##&{reset}{red}@@@@@@@@@@##&{reset}@@@{reset}")
    print(f"@@@{red}&##@@@@@@@@@@@@{blue}&##&{reset}@@@@@@@@@@@@@@@@{blue}&##&{reset}{red}@@@@@@@@@@@@##&{reset}@@@{reset}")
    print(f"@@@{red}&##@@@@@@@@@@@@@@{blue}##&&{reset}@@@@@@@@@@{blue}&&##&{reset}{red}@@@@@@@@@@@@@@##&@{reset}@@@{reset}")
    print(f"@@@{red}&##@@@@@@@@@@@@@@@{blue}&####&{reset}@@@@@@{blue}&####&{reset}{red}@@@@@@@@@@@@@@@##&{reset}@@@{reset}")
    print(f"@@@{red}&##@@@@@@@@@@@@@{blue}&##&@{reset}&&{blue}##&{reset}@@&{blue}##&&{reset}{blue}{red}@&##&@@@@@@@@@@@@@{red}##&{reset}@@@{reset}")
    print(f"@@@{red}&##@@@@@@@@@@@{blue}&##&@{reset}@@@@@{blue}&####&{reset}@@@{blue}@@@&##{reset}{red}&&@@@@@@@@@@##&{reset}@@@{reset}")
    print(f"@@@{red}&##@@@@@@@@{blue}&&##&@{reset}@@@@@@@@@{blue}&&{reset}@@@@@@@@{blue}@@&&#{reset}{red}#&@@@@@@@@##&{reset}@@@{reset}")
    print(f"@@@{red}&##@@@@@@{blue}&##&&@{reset}@@@@@@@@@@@@@@@@@@@@@@@{blue}@@&&##&{reset}{red}@@@@@@##&{reset}@@@{reset}")
    print(f"@@@{red}&##@@@@{blue}&##&@{reset}@@@@@@@@@@@@@@@@@@@@@@@@@@@@@{blue}@@&##&{reset}{red}@@@@##&{reset}@@@{reset}")
    print(f"@@@{red}@&#&@@{reset}@&&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&&@{red}@@&#&@{reset}@@@")
    print(f"@@@@@&##&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&##&@@@@@")
    print(f"@@@@@@@&&##########################################&&@@@@@@@")
    sleep(1)
    print("\n")
    print("\n")
    print("   Created by Fattcat --> https://github.com/Fattcat")
    print(f"               {green}+{reset}-------------------------{green}+{reset}")
    print(f"               {green}+{reset}         {green}Welcome{reset}         {green}+{reset}")
    print(f"               {green}+{reset}           To            {green}+{reset}")
    print(f"               {green}+{reset}-------------------------+{reset}")
    print(f"               {green}+{reset}  {red}Mail Sender / Pranker{reset}  +{reset}")
    print(f"               {green}+{reset}-------------------------+{reset}")
    print("\n")
    print("\n")

def Settings():
    print("lol")


MailLogo()
sleep(2)
os.system("clear")
print("\n")
print("\n")
print("\n")
print("[ 1 ] Send Some Email Message to someone")
print("[ 1 ] Settings")
print("[ 1 ] EXIT")

Choice = input("         Select Option --> ")

if Choice == "1":
    print("NENI SOM DOKONCENY, mam nastavit Meno a Heslo gmail a odoslat to niekomu pomocou SPAMU kazde @ sekundy nejaku spravu")
elif Choice == "2":
    Settings()
elif Choice == "3":
    exit()
else:
    print("Bad Option Please Select something else !\nCANCELLING ...")
    
