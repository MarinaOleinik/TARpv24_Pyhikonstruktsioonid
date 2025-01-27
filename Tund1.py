from random import *
#3
kommide_arv=randint(10,100)
print(f"Laua peal on {kommide_arv}")
mitu=int(input("Mitu tahad süüja?"))
print(f"Laua peal on jäänud {kommide_arv-mitu}")


#2
vanus = 18
eesnimi = "Jaak"
pikkus = 16.5
kas_käib_koolis = True
print(f"Muutuja {vanus} on {type(vanus)}")
print(f"Muutuja {eesnimi} on {type(eesnimi)}")
print(f"Muutuja {pikkus} on {type(pikkus)}")
print(f"Muutuja {kas_käib_koolis} on {type(kas_käib_koolis)}")

#1
print("Tere maailm!")
nimi=input("Mis on sinu nimi? ").capitalize()
print(f"Tere maailm!, Tervitan sind {nimi}")
vanus=int(input("Kui vana sa oled?"))
print(f"Tere maailm!, Tervitan sind {nimi}! Sa oled {vanus} aastat vana.")