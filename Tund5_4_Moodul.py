
p=[]
i=[]
def Lisa_andmed(p:list,i:list):
    """
    """
    while True:
        try:
            nimi=input("Nimi: ")
            if nimi.isalpha():
                try:
                    palk=float(input("Palk:"))
                except:
                    print("Palk on arv!")
                break
        except:
            print("Kirjuta ainult tähtede kasutades")
    p.append(palk)
    i.append(nimi)

def Kustuta_andmed(p:list,i:list):
    """
    """
    try:
        nimi=input("Nimi: ")
        if nimi.isalpha():
            k=i.count(nimi)
            if k>0:
                for j in range(k):
                    ind=i.index(nimi)
                    i.pop(ind)
                    p.pop(ind)
                print("Andmed on kustutatud")
            else:
                print("Andmed puuduvad!")
    except:
        print("Kirjuta ainult tähtede kasutades")

def Suurim_palk(p:list,i:list):
    """
    """
    suurim=max(p)
    print(f"Suurim palk on {suurim}")
    k=p.count(suurim)
    ind=p.index(suurim)
    for j in range(k):
        ind=p.index(suurim,ind)
        print(f"Saab kätte {i[ind]}")
        ind+=1

def Sorteerimine(p:list,i:list):
    """
    """
    v=input("Vali märk: > (kasvav) või < (kahanev)")#Try except koos while True'ga
    for n in range(0,len(i)):
        for m in range(n,len(i)):
            if eval(str(p[n])+v+str(p[m])): #p[n]>p[m]
                p[n],p[m]=p[m],p[n]
                i[n],i[m]=i[m],i[n]
   
def Võrdsed_palgad(p:list,i:list):
    """
    """
    hulk=set(p) #{element1, element2...}
    print(hulk)
    for palk in hulk:
        k=p.count(palk)
        if k>1:
            print(f"Palk {palk}")
            ind=p.index(palk)
            for j in range(k):
                ind=p.index(palk,ind)
                print(f"Saab kätte {i[ind]}")
                ind+=1
        
