import random

print("Выберите уровень сложности:")
print("1. Легкий")
print("2. Средний")
print("3. Сложный")
try:
    difficulty = int(input("Введите номер сложности (1, 2 или 3): "))

except ValueError:
    print("Ошибка: Введите целое число (1, 2 или 3).")























from Moodul_Tund6 import *
#arithmetic funktsiooni kasutamine
a=float(input("Sisesta arv 1: "))
b=float(input("Sisesta arv 2: "))
t=input("Tehe: ")
v=arithmetic(a,b,t)
print(v)
#is_year_leap funktsiooni kasutamine
aasta=int(input("Mis aasta tahad kontrollida? "))
if aasta>0: 
    v=is_year_leap(aasta)
    print(v)
    if v:
        print(f"{aasta} on liigaasta")
    else:
        print(f"{aasta} ei ole liigaasta")
#square funktsiooni kasutamine
S,P,d=square(float(input("Sisesta külg")))
print(S,P,d)
#square_list kasutamine, tee ise