import tkinter as tk
import random

pencere = tk.Tk()
pencere.title("Letters From Pelican Town")
pencere.geometry("600x400")


def mektup_ac():
    mektuplar = [
        """📩

Dear Eftun,

Someone in Pelican Town thinks you are pretty cool.

🌿
""",
        """📩

Dear Eftun,

This letter was delivered by a farmer named İlayda.

❤️
""",
        """📩

Dear Eftun,

Don't forget to take care of yourself today.

🌻
"""
    ]

    secilen = random.choice(mektuplar)
    mektup.config(text=secilen)


baslik = tk.Label(
    pencere,
    text="A small collection of letters for Eftun <3",
    font=("Arial", 12)
)
baslik.pack(pady=10)

mektup = tk.Label(
    pencere,
    text="📩 Press the button to open a letter",
    font=("Arial", 12),
    wraplength=450,
    justify="center"
)
mektup.pack(pady=30)

buton = tk.Button(
    pencere,
    text="📩 Open Letter",
    command=mektup_ac,
    font=("Arial", 12)
)
buton.pack()

pencere.mainloop()