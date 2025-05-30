from tkinter import *
k=0
def vajutatud():
    global k
    k+=1
    pealkiri.config(text=f"Sa vajutasid nuppu! {k} korda!")
    nupp.config(text="Vajuta veel kord!", bg="orange", fg="blue")
def vajutatudPK(event):
    global k
    k-=1
    pealkiri.config(text=f"Sa vajutasid nuppu! {k} korda!")
    nupp.config(text="Vajuta veel kord!", bg="blue", fg="orange")
def tuhista(event):
    sisetus.delete(0, END)   
    # sisetus.unbind("<FocusIn>")
    # sisetus.bind("<FocusOut>", tagasi))    
def saadamuutuja(event):
    muutuja=sisetus.get()
    pealkiri.config(text=f"Sa sisestasid: {muutuja}")

aken=Tk()
aken.title("Teema 8")
aken.geometry("400x400")
aken.configure(bg="lightblue")
#aken.resizable(width=False, height=False)
aken.iconbitmap("Poke-Ball.ico")


pilt = PhotoImage(file="bee.png")
lbl_piltiga=Label(aken, image=pilt)



pealkiri=Label(aken, text="Tere tulemast Teema 8!", bg="lightblue", font=("Arial", 16),fg="green")
nupp=Button(aken, text="Vajuta mind!", bg="yellow", font=("Arial", 12),activebackground="grey", fg="green", relief=RAISED,command=vajutatud)#SUNKEN, RAISED, GROOVE, and RIDGE
nupp.bind("<Button-3>",vajutatudPK)
sisetus=Entry(aken, bg="white", font=("Arial", 12), fg="black")
sisetus.insert(0, "Sisesta midagi siia") #END
sisetus.bind("<FocusIn>",tuhista)
sisetus.bind("<Return>",saadamuutuja)


pealkiri.pack(pady=20)
sisetus.pack(pady=20)
nupp.pack(pady=20)
lbl_piltiga.pack(pady=20)

aken.mainloop()
