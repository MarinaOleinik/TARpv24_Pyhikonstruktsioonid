
import os
from random import *
import subprocess
import colorama
from colorama import Fore, Style
from colorama import just_fix_windows_console
colorama.just_fix_windows_console()
colorama.init(autoreset=True)  # Включает поддержку ANSI в Windows

print(Fore.RED + "Этот текст должен быть красным")
print(Fore.GREEN + "А этот – зеленым")
sõne="Programmeerimine"
print(sõne)
print("\033c", end="")
subprocess.run("cls", shell=True)
os.system('cls')
sõne_list=list(sõne)
print(sõne_list)

sõne_list.reverse()
print(sõne_list)
print(sõne_list.index("P"))
print(len(sõne_list))
print(len(sõne))

kogus_m=sõne_list.count("m")
for m in range(kogus_m):
    sõne_list.remove("m")
tähed=randint(1,10)
for i in range(tähed):
    while 1:
        try:
            t=input("Sisesta täht: ")
            if t.isalpha(): break
        except:
            print("On vaja täht!")
    sõne_list.append(t)
print(sõne_list)
tähed=randint(1,6)
for i in range(tähed):
    while 1:
        try:
            t=input("Sisesta täht: ")
            if t.isalpha(): break
        except:
            print("On vaja täht!")
    while 1:
        try:
            ind=input("Sisesta index: ")
            if ind.isnumeric() & int(ind)<len(sõne_list): break
        except:
            print("On vaja index!")
    sõne_list.insert(int(ind),t)
print(sõne_list)
def funktion(e):
    return len(e)
sõne_list.sort(reverse=True, key=funktion)
print(sõne_list)