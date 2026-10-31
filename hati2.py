import streamlit as st
import random
from PIL import Image, ImageTk
import os

# ================== PENCERE ==================
root = tk.Tk()
root.title("Hatice ❤️")
root.attributes("-fullscreen", True)
root.configure(bg="gray")

W = root.winfo_screenwidth()
H = root.winfo_screenheight()

# ================== FOTO ==================
def load(path):
    img = Image.open(path)
    img = img.resize((550, 650))  # 📌 RESİMLER BÜYÜDÜ
    return ImageTk.PhotoImage(img)

images = {
    "giris": load("giris.jpg"),
    "walle": load("walle.jpg"),
    "dissiz": load("dissiz.jpg"),
    "final1": load("final1.jpg"),
    "final3" : load("final3.jpeg"),
    "final2": load("final2.jpg"),

}

# ================== KALP YAĞMURU ==================
canvas = tk.Canvas(root, width=W, height=H, bg="red", highlightthickness=0)
canvas.place(x=0, y=0)

hearts = []

def create_heart():
    x = random.randint(0, W)
    size = random.randint(18, 35)
    heart = canvas.create_text(x, 0, text="❤️", font=("Arial", size))
    speed = random.randint(2, 6)
    hearts.append([heart, speed])

def move_hearts():
    for h in hearts[:]:
        canvas.move(h[0], 0, h[1])
        pos = canvas.coords(h[0])
        if pos[1] > H:
            canvas.delete(h[0])
            hearts.remove(h)
    root.after(40, move_hearts)

def spawn_hearts():
    create_heart()
    root.after(150, spawn_hearts)

# ================== FRAME ==================
frame = tk.Frame(root, bg="white")
frame.place(relwidth=1, relheight=1)

def clear():
    for w in frame.winfo_children():
        w.destroy()

# ================== ORTA SAĞ YAZI ==================
def add_text(title, text):
    tk.Label(
        frame,
        text=title,
        font=("Arial", 34, "bold"),
        bg="white"
    ).place(relx=0.48, rely=0.2)  # 📌 SAĞA ALINDI

    tk.Label(
        frame,
        text=text,
        font=("Arial", 18),
        bg="white",
        justify="center"
    ).place(relx=0.65, rely=0.35)

# ================== EKRAN ==================
def screen(img_key, title, text, btn, next_func):
    clear()

    tk.Label(frame, image=images[img_key], bg="white").place(relx=0.1, rely=0.15)

    add_text(title, text)

    tk.Button(
        frame,
        text=btn,
        font=("Arial", 25),
        command=next_func
    ).place(relx=0.50, rely=0.75)

# ================== SAYFALAR ==================
def acilis():
    screen(
        "giris",
        "🎂 Doğum Günün Kutlu OLSUUNN❤️",
        "küçük bir sürpriz hazırladım ve fotolar nnne alaka \nbilmiyorum .",
        "🎁 bass bakalim",
        walle
    )

def walle():
    screen(
        "walle",
        "🤖 WALL-E EVEEE",
        "İLK İZLDİGİMİZ VE HAKKINDA KONUSTUGUMUZ \nANİMASYON oldugu \nicin onlari ayri biz diye seviyorum❤️",
        "⭐ letssgooooo",
        dissiz
    )

def dissiz():
    screen(
        "dissiz",
        "🐉 Dişsiz ve İSİGİN OFKESİ YANİ BİZ ",
        "benim için cok cok cok özelsinbal petegim \nİyi kiiiiii varsın❤️",
        "📸 devam ediyoruz",
        final1
    )

def final1():
    screen(
        "final1",
        "❤️❤️",
        "Bugün senin günün.\nİyi ki doğdun AŞKIMMMM❤️",
        "💌 devams",
        final3
    )
def final3():
    screen(
        "final3",
        "STARDEEWWWW",
        "twdan rastgele bi gece dmlesip tanıstıgım kızla \ngeldigim son nokta❤️",
        "⭐ finito son1",
        final2
    )
# ================== SON SAYFA (BUTON + KALP GARANTİ) ==================

def final2():
    clear()

    tk.Label(frame, image=images["final2"], bg="white").place(relx=0.1, rely=0.15)

    tk.Label(
        frame,
        text="SENİ ÇOK SEVİYORUM OMRUMM❤️",
        font=("Arial", 35, "bold"),
        fg="red",
        bg="white"
    ).place(relx=0.47, rely=0.2)

    tk.Label(
        frame,
        text="artık tum doğum günlerini \nbirlikte kutlamak dileğiyle bebegimm..❤️",
        font=("Arial", 25),
        bg="white"
    ).place(relx=0.50, rely=0.4)

    tk.Button(
        frame,
        text="❤️biitttiii❤️",
        font=("Arial", 18),
        command=root.destroy
    ).place(relx=0.7, rely=0.7)

# ================== BAŞLAT ==================
root.bind("<Escape>", lambda e: root.destroy())

acilis()
spawn_hearts()
move_hearts()

root.mainloop()
