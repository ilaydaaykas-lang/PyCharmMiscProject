import tkinter as tk
import random
from PIL import Image, ImageTk

pencere = tk.Tk()
pencere.title("A small collection of letters for Eftun<3")
pencere.geometry("600x600")

from PIL import Image, ImageTk


resim = Image.open("stardew.jpg")
resim = resim.resize((700, 400))
bg = ImageTk.PhotoImage(resim)


arkaplan = tk.Label(pencere, image=bg)
arkaplan.place(x=0, y=0)

def mektup_ac():
    mektuplar = [
        """Dear Eftun,

Someone in Pelican Town thinks you're pretty cool 🌿""",
        """Dear Eftun,

This letter was delivered by İlayda ❤️""",
        """Dear Eftun,

Don't forget to smile today 🌻"""
    ]

    mektup.config(text=random.choice(mektuplar))


baslik = tk.Label(
    pencere,
    text="A small collection of letters for Eftun<3",
    font=("Arial", 15),
    bg="white"
)
baslik.pack(pady=15)

mektup = tk.Label(
    pencere,
    text="Press the button to open a letter",
    font=("Arial", 11),
    wraplength=550,
    justify="center",
    bg="white"
)
mektup.pack(pady=30)

buton = tk.Button(
    pencere,
    text="Open Letter",
    command=mektup_ac
)
buton.pack()

pencere.mainloop()