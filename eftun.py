import tkinter as tk
import random
pencere= tk.Tk()
pencere.title(" Letters From Pelican Town")
pencere.geometry("600x400")
def mektup_ac():
    var = [
        """📩
        
        Dear Eftun,
        
        Someone in Pelican Town thinks you are pretty cool.""",

        """Dear Eftun,
        
        This letter was delivered by a farmer named İlayda"""],

secilen = random.choice(mektup_ac)
mektup.config(text=secilen)
baslik=tk.Label(pencere,text="A small collection of letters for Eftun<3",font=("Arial",11))
baslik.pack(pady=20)
mektup = tk.Label(
    pencere,
    text="📩 Press the button to open a letter",
    font=("Arial", 12),
    wraplength=450,
    justify="center")
mektup.pack(pady=30)
buton = tk.Button(
    pencere ,
    text="📩 Open Letter",
    command=mektup_ac,
    font=("Arial", 12))
buton.pack()

pencere.mainloop()
