#Random ja list kasutamine
from random import *
tehed=["+","-","*","/"]
valitud_tehe=choice(tehed)
print(valitud_tehe)
if valitud_tehe=="+":
    print("Oli valitud summa")

a=randint(0,5)
b=randint(0,5)
print(f"Millega võrdub {a} {valitud_tehe} {b} =")
vastus=int(input("Anna vastus:"))
if vastus==eval(str(a)+valitud_tehe+str(b)):
    print("Tore!")
else:
    print("Vale!")

#Ülesanne 10
print("Ülesanne 10")
for j in range(10):
    a1=float(input("Esimene arv: "))
    a2=float(input("Teine arv: "))
    if a1>a2:
        print(f"Suurem on {a1}")
    elif a2>a1:
        print(f"Suurem on {a2}")
print()
#Ülesanne 15
print("Ülesanne 15")
for j in range(10):
    for i in range(10):
        print(i,end=" ")
    print()
print()
#Ülesanne 5
print("Ülesanne 5")
summa=0
while True:
    try:
        N=int(input("Sisesata N:"))
        if N>=1:
            for i in range(1,N+1):
                arv=float(input(f"Sisesta {i}. arv: "))
                if arv<0:
                    summa+=arv
            print(f"Summa võrdub {summa}-ga")
            break
        else:
            print("Arv A peab olema rohkem kui 1")
    except:
        print("Vale formaat")



#Ülesanne 2
print("Ülesanne 2")
summa=0
while True:
    try:
        A=int(input("Sisesata A:"))
        if A>1:
            for i in range(1,A+1):
                summa+=i
            print(f"Summa võrdub {summa}-ga")
            break
        else:
            print("Arv A peab olema rohkem kui 1")
    except:
        print("Vale formaat")




#Ülesanne 1
print("Ülesanne 1")
täisarvud=0
for i in range(15):
    while True:
        try:
            arv=float(input(f"Sisesta {i+1}. arv"))
            break
        except:
            print("Kirjuta ainult numbrid")
    # 2.5 int(2.5)=2 
    if arv==int(arv): täisarvud+=1
print(f"Täisarvude kogus: {täisarvud}")





print("Tere! Olen sinu uus sõber - Python!")
nimi=input("Sisesta oma nimi: ")
print(f"{nimi}, oi kui ilus nimi! ")
while 1:
    try:
        soov=int(input(f"{nimi}! Kas leian Sinu keha indeksi? 0-ei, 1-jah =>"))
        if soov==1:
            print("Indeksi leidmine")
            while True:
                try:
                    pikkus=int(input("Mis on sinu pikkus? "))
                    break
                except:
                    print("Vale pikkuse formaat!")
            while True:       
                try:
                    mass=float(input("Mis on sinu kaal? "))
                    break
                except:
                    print("Vale kaalu formaat!")
            indeks=round(mass/(0.1*pikkus)**2,2)
            print(nimi,"! Sinu keha indeks on:" ,indeks)
            #If
            break
        elif soov==0:
            print("Kahju! See on väga kasulik info!")
            break
        else:
            print("Vale valik. Saab valida ainult 1 või 0")
    except:
        print("Vale soov!")
