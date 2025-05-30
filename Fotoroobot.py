
from tkinter.messagebox import showinfo
import customtkinter as ctk
from tkinter import simpledialog,Canvas
from PIL import Image, ImageTk
import pygame
# Andmestruktuurid
pildid = {}
objektid = {}
olemas = {}  # Jälgib, kas osa on hetkel canvas'il
def salvesta_nägu():
    # Küsi faili nimi
    failinimi = simpledialog.askstring("Salvesta pilt", "Sisesta faili nimi (ilma laiendita):")
    if not failinimi:
        return  # tühistati

    # Tühi alus (valge taust, 400x400)
    lõpp_pilt = Image.new("RGBA", (400, 400), (255, 255, 255, 255))
    # Koosta nägu – ainult need osad, mis on olemas
    for nimi in ["nägu", "otsmik", "silmad", "nina", "suu"]:
        if olemas.get(nimi):
            failitee = {
                "nägu": "alus.png",
                "otsmik": "otsmik1.png",
                "silmad": "silmad1.png",
                "nina": "nina1.png",
                "suu": "suu1.png"
            }.get(nimi)
            if failitee:
                osa = Image.open(failitee).convert("RGBA").resize((400, 400))
                lõpp_pilt.alpha_composite(osa)
    # Salvesta
    lõpp_pilt.save(f"{failinimi}.png")
    showinfo("Pilt salvestatud:",f"Faili nimi on {failinimi}.png")
# Üldfunktsioon osa lisamiseks/eemaldamiseks
def toggle_osa(nimi, fail, x, y):
    if olemas.get(nimi):
        canvas.delete(objektid[nimi])
        olemas[nimi] = False
    else:
        pil_img = Image.open(fail).convert("RGBA").resize((400, 400))
        tk_img = ImageTk.PhotoImage(pil_img)
        pildid[nimi] = tk_img
        objektid[nimi] = canvas.create_image(x, y, image=tk_img)
        olemas[nimi] = True

def mängi_muusika():
    pygame.mixer.music.play(loops=-1)
def peata_muusika():
    pygame.mixer.music.stop()
pygame.mixer.init()
pygame.mixer.music.load("taustamuusika.mp3")

app = ctk.CTk()
app.geometry("800x500")
app.title("Näo koostaja nuppudega")

# Canvas paremal
canvas = Canvas(app, width=400, height=400, bg="white")
canvas.pack(side="right", padx=10, pady=10)

# Lisa ALUS kohe (näo ovaal)
toggle_osa("nägu", "alus.png", 200, 200)
olemas["nägu"] = True  # märgime, et see on olemas

# Vasak paneel nuppudega
frame = ctk.CTkFrame(app)
frame.pack(side="left", padx=10, pady=10)
seaded = {
    "width": 150, "height": 40, 
    "font": ("Segoe UI Emoji", 32),
    "fg_color": "#4CAF50",
    "text_color": "white",
    "corner_radius": 20 }
# Nupud näoosadele
ctk.CTkLabel(frame, text="😎 Vali näoosad:",**seaded).pack(pady=5)
ctk.CTkButton(frame, text="🧢 Otsmik", command=lambda: toggle_osa("otsmik", "otsmik1.png", 200, 200),**seaded).pack(pady=3)
ctk.CTkButton(frame, text="👀 Silmad", command=lambda: toggle_osa("silmad", "silmad1.png", 200, 200),**seaded).pack(pady=3)
ctk.CTkButton(frame, text="👃 Nina", command=lambda: toggle_osa("nina", "nina1.png", 200, 200),**seaded).pack(pady=3)
ctk.CTkButton(frame, text="👄 Suu", command=lambda: toggle_osa("suu", "suu1.png", 200, 200),**seaded).pack(pady=3)
nupp = ctk.CTkButton(frame, text="💾 Salvesta nägu", command=salvesta_nägu,**seaded)
nupp.pack(pady=10)

frame_mus = ctk.CTkFrame(frame)
frame_mus.pack(padx=10, pady=10)
ctk.CTkButton(frame_mus, text="▶️ Mängi muusikat",fg_color="#4CAF50", command=mängi_muusika).pack(side="left",pady=10)
ctk.CTkButton(frame_mus, text="⏹️ Peata muusika", fg_color="#4CAF50",command=peata_muusika).pack(side="left",pady=10)
# Käivita aken
app.mainloop()
