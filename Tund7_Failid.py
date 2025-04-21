import smtplib,ssl
from email.message import EmailMessage
from tkinter import filedialog
#https://myaccount.google.com/apppasswords Rakenduste paroolid
def saada_kiri():
    kellele=input("Kellele saata: ")
    teema=input("Teema: ")
    #sisu=input("Sisu: ")
    smtp_server='smtp.gmail.com'
    smtp_port=587
    kellelt="oleinik.marina@gmail.com"
    salasõna=input("Salasõna: ") #wjaa grry wecm lmhj 
    msg=EmailMessage()
    msg['Subject']=teema
    msg['From']=kellelt
    msg['To']=kellele   
    sisu="""
    <!DOCTYPE html>
    <head>
    </head>
        <body>
            <h1>Oleinik tunniplaan</h1>
            <p>Tere,</p>
            <a href="https://thk.edupage.org/timetable/view.php?fullscreen=1">Minu tunniplaan!</a>
        </body>
    </html>
"""
    msg.set_content(sisu,subtype='html')
    fail=filedialog.askopenfilename(title="Vali fail",filetypes=[("All files","*.*")])
    with open(fail,'rb') as f:
        faili_sisu=f.read()
        faili_nimi=fail.split("/")[-1]
        msg.add_attachment(faili_sisu,maintype="application",subtype="octet-stream",filename=faili_nimi)
    try:
        with smtplib.SMTP(smtp_server,smtp_port) as server:
            server.starttls(context=ssl.create_default_context())
            server.login(kellelt,salasõna)
            server.send_message(msg)
        print("Kiri saadetud!")
    except Exception as e:
        print("Viga:",e)

saada_kiri()

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
