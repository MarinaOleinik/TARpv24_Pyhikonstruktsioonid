
def Loe_failist(fail:str)->list:
    f=open(fail,'r',encoding="utf-8-sig")
    jarjend=[]
    for rida in f:
        jarjend.append(rida.strip())
    f.close()
    return jarjend
def Kirjuta_failisse(fail:str,jarjend:list):
    f=open(fail,'w',encoding="utf-8-sig")
    for line in jarjend:
        f.write(line+'\n')
    f.close()


list_=Loe_failist("Tund7.txt")
for x in list_:
    print(x)

list_=["Ann","Kati","Mari"]
Kirjuta_failisse("Tund7.txt",list_)
list_2=Loe_failist("Tund7.txt")
print(list_2)
with open("Tund7.txt","r",encoding="utf-8-sig") as f:
    print(f.read())
