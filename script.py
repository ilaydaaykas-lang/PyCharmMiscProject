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
