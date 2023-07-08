import os
from time import sleep
import smtplib
import platform
import subprocess
import random

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

os.system("clear")

def CheckOS():
    sleep(1)
    OS = platform.system()
    if OS == "Windows":
        print(f"                        {magenta}+{reset} --------------------------------- +")
        print(f"                     + Detected Operation System :  {green}Windows{reset} +")
        print(f"                       + {green} Linux is BETTER than Windows{reset} +")
        print(f"                        + --------------------------------- {magenta}+{reset}")
        sleep(2)
    elif OS == "Linux":
        print(f"                        {magenta}+{reset} --------------------------------- {green}+{reset}")
        print(f"                        + Detected Operation System : {green}Linux{reset} +")
        print(f"                        +   Is perfect to control Linux OS  +")
        print(f"                        {green}+{reset} --------------------------------- {magenta}+{reset}")
        sleep(2)
    else:
        print(f"                         {red}+{reset} -------------------------------------- {red}+{reset}")
        print(f"                        +{red}  Unknown Operation System{reset} {orange}!{reset} +")
        print(f"                         {red}+{reset} -------------------------------------- {red}+{reset}")
        sleep(1)
        print("Dont Worry ...")
        sleep(2)
CheckOS()

def MailLogo():
    os.system("clear")
    sleep(0.3)
    print(f"               {green}+{reset}-------------------------{green}+{reset}")
    print(f"               {green}+{reset}         {green}Welcome{reset}         {green}+{reset}")
    print(f"               {green}+{reset}           To            {green}+{reset}")
    print(f"               {green}+{reset}-------------------------{green}+{reset}")
    print(f"               {green}+{reset}  {red}Mail Sender / Pranker{reset}  {green}+{reset}")
    print(f"               {green}+{reset}-------------------------{green}+{reset}")
    print("   Created by Fattcat --> https://github.com/Fattcat")
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
    print("\n")
    print(f"         {magenta}[{reset} -------- {magenta}]{reset} {blue}MAIL{reset} - {blue}S{reset}{red}3{reset}{blue}nd{reset}{red}3{reset}{red}R{reset} {magenta}[{reset} -------- {magenta}]{reset}")
    print("     Send Something to anyone OR Prank Your Friends")

def Settings():
    print("lol")


MailLogo()
#os.system("clear")
print(f"{magenta}[{reset} {green}1{reset} {magenta}]{reset} Send Some Email Message to someone")
print(f"{magenta}[{reset} {green}2{reset} {magenta}]{reset} Settings")
print(f"{magenta}[{reset} {green}3{reset} {magenta}]{reset} EXIT")
print("\n")

Choice = input("--> ")

if Choice == "1":
    subprocess.run(["python3", "mail.py"])
    print("NENI SOM DOKONCENY, mam nastavit Meno a Heslo gmail a odoslat to niekomu pomocou SPAMU kazde @ sekundy nejaku spravu")
elif Choice == "2":
    Settings()
elif Choice == "3":
    pass # SEM MA IST RANSOM MODUL 
         # A MA AJ VYBRAT NAHODNY 1 GMAIL ucet s HESLOM s Lail-List.py
elif Choice == "4":
    os.system("clear")
    exit()
else:
    print("Bad Option Please Select something else !\nCANCELLING ...")
    
