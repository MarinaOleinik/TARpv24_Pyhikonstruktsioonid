from datetime import *
from calendar import *
from math import *
#Ülesanne 7"
try:
    a=float(input("A: "))
    b=float(input("B: "))
    if a>0 and b>0:
        print("Pindala ja ümbermõõdu arvutamine: ")
        S=a*b
        P=(a+b)*2
        print(f"S={S}, P={P}")
    else:
        print("Arvud peavad suurem kui 0 olla!")
except:
    print("Vale andmed!")

#Ülesanne 5"
# kill-koll kill-koll
# killadi-koll 
# kill-koll kill-koll 
# killadi-koll 
# kill-koll kill-koll kill-koll kill-koll
a="kill-koll ".capitalize()
b="killadi-koll ".capitalize()
print(a*2,b,a*2,b,a*4)



#"Ülesanne 4"
d=2.575 # mündi d sm
maaR=6378 # maa radius km
maaR*=100000 # maa radium sm
Pmaa=2*pi*maaR # maa ümbermõõt
kogus=Pmaa/d

print(f"Meil on vaja {int(kogus):,d} mündi.")
print(f"Meil on vaja {int(kogus*2):,d} euro.")

#"Ülesanne 3"
try:
    R=float(input("R: "))
    Sruudu=round((2*R)**2,2)
    Sringi=round(pi*R**2,2)
    Pruudu=round(8*R,2)
    Pringi=round(2*pi*R,2)
    print(f"Vastus:\nRuudu pindala on {Sruudu}, Ruudu ümbermõõt on {Pruudu}, \nRingi pindala on {Sringi}, Ringi ümbermõõt on {Pringi}.")
    print()
except:
    print("Sisesta ujukomaarvud!")
#"Ülesanne 2"
a=3 + 8 / (4 - 2) * 4

#"Ülesanne 1"
tana=date.today()
print(f"Tere! Täna on {tana}")

# 27/12/2022
tana_ = tana.strftime("%d/%m/%Y")
print(f"Tere! Täna on {tana_}")
paevadekogus=monthrange(2025,1)[1]
print(f"Jaanuaris on {paevadekogus} päeva")
päevad=tana.day
onjäänud=paevadekogus-päevad
print(f"Jaanuaris on jäänud {onjäänud} päeva")
#1.V
aastalõpuni=onjäänud+monthrange(2025,2)[1]+monthrange(2025,3)[1]+monthrange(2025,4)[1]+monthrange(2025,5)[1]+monthrange(2025,6)[1]+monthrange(2025,7)[1]+monthrange(2025,8)[1]+monthrange(2025,9)[1]+monthrange(2025,10)[1]+monthrange(2025,11)[1]+monthrange(2025,12)[1]
print(f"Aasta lõpuni on jäänud {aastalõpuni}")
#2.V
aastalõpuni=365-monthrange(2025,1)[1]+onjäänud
print(f"Aasta lõpuni on jäänud {aastalõpuni}")





# # December 27, 2022
# # tana_ = tana.strftime("%B %d, %Y")
# # print(f"Tere! Täna on {tana_}")

# # 12/27/22
# # tana_ = tana.strftime("%m/%d/%y")
# # print(f"Tere! Täna on {tana_}")

# # Dec-27-2022
# # tana_ = tana.strftime("%b-%d-%Y")
# # print(f"Tere! Täna on {tana_}")