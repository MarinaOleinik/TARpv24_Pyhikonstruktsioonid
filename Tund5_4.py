from Tund5_4_Moodul import *

palgad=[1200,2500,750,395,1200]
inimesed=["A","B","C","D","E"]

while True:
    print("Andmed:")
    print(inimesed)
    print(palgad)
    print("Vajuta:\n1-Andmete lisamiseks\n2-Andmete kustutamiseks nime järgi\n3-Suurima palga leidmiseks\n4-Andmete sortimiseks\n5-Võrdsete palgade leidmiseks")
    v=int(input())
    if v==1:
        k=int(input("Mitu inimest? "))
        for i in range(k):
            Lisa_andmed(palgad,inimesed)
    elif v==2:
        Kustuta_andmed(palgad,inimesed)
    elif v==3:
        Suurim_palk(palgad,inimesed)
    elif v==4:
        Sorteerimine(palgad,inimesed)
    elif v==5:
        Võrdsed_palgad(palgad,inimesed)
