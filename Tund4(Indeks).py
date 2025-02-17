print("Tere! Olen sinu uus sõber - Python!")
nimi=input("Sisesta oma nimi: ")
print(f"{nimi}, oi kui ilus nimi! ")
try:
    soov=int(input(f"{nimi}! Kas leian Sinu keha indeksi? 0-ei, 1-jah =>"))
    if soov==1:
        print("Indeksi leidmine")
        try:
            pikkus=int(input("Mis on sinu pikkus? "))
            try:
                mass=float(input("Mis on sinu kaal? "))
                indeks=round(mass/(0.1*pikkus)**2,2)
                print(nimi,"! Sinu keha indeks on:" ,indeks)

            except:
                print("Vale kaalu formaat!")
        except:
            print("Vale pikkuse formaat!")
    elif soov==0:
        print("Kahju! See on väga kasulik info!")
    else:
        print("Vale valik. Saab valida ainult 1 või 0")
except:
    print("Vale soov!")