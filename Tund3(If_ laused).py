
from random import *
#Näidis 1
arv=randint(0,10)
print(arv)
if arv>5:
    print("***********************")
    print(f"Arv {arv} suurem kui 5")
    print("***********************")
if arv>5: print(f"Arv {arv} suurem kui 5")

#Näidis 2
arv=randint(-10,10)
if arv>0:
    print("Positiivne")
else:
    print("Negatiivne") #viga!

if arv>0:
    print("Positiivne")
elif arv==0:
    print("0")
else:
    print("Negatiivne")
#a Kui eesnimi on Juku siis lähme Jukuga kinno. Aga teeme seda nii, kui nimi oli kirjutatud suurtähtedega.
print("Kino")
nimi=input("Mis on sinu nimi?")
if nimi.isupper() and nimi.lower()=="juku":
    print("Lähme kinno")
    try:
        vanus=int(input("Kui vana sa oled?"))
        if vanus<0 or vanus>100:
            pilet="!!!"
        elif vanus<6:
            pilet="Tasuta"
        elif vanus<=14:
            pilet="Lastepilet"
        elif vanus<=65:
            pilet="Täispilet"
        elif vanus<=100:
            pilet="Sooduspilet"
        print(pilet)
    except Exception as e:
        print("Tekkis viga: ",e)
else:
    print("Ma olen hõivatud")