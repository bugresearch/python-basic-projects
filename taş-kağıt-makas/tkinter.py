import tkinter as tk
from tkinter import messagebox
import random

def tas():
    data = ["Taş", "Kağıt", "Makas"]
    rastgele = random.randint(0, 2)
    tahmin = data[rastgele]
    if rastgele == 0:
        print("Berabere")
        text = "Tahminim ",tahmin,"\n Berabere Bitti"
    elif rastgele == 1:
        print("Bilgisayar Kazandı")
        text = "Tahminim ", tahmin, "\n Ben Kazandım"
    elif rastgele ==2:
        print("Kullanıcı Kazandı")
        text = "Tahminim ", tahmin, "\n Kazandın"
    var = messagebox.showinfo("Hesap Makinesi", text)


def kagit():
    data = ["Taş", "Kağıt", "Makas"]
    rastgele = random.randint(0, 2)
    tahmin = data[rastgele]
    if rastgele == 1:
        print("Berabere")
        text = "Tahminim ",tahmin,"\n Berabere Bitti"
    elif rastgele == 2:
        print("Bilgisayar Kazandı")
        text = "Tahminim ", tahmin, "\n Ben Kazandım"
    elif rastgele ==0:
        print("Kullanıcı Kazandı")
        text = "Tahminim ", tahmin, "\n Kazandın"
    var = messagebox.showinfo("Hesap Makinesi", text)

def makas():
    data = ["Taş", "Kağıt", "Makas"]
    rastgele = random.randint(0, 2)
    tahmin = data[rastgele]
    if rastgele == 2:
        print("Berabere")
        text = "Tahminim ",tahmin,"\n Berabere Bitti"
    elif rastgele == 0:
        print("Bilgisayar Kazandı")
        text = "Tahminim ", tahmin, "\n Ben Kazandım"
    elif rastgele ==1:
        print("Kullanıcı Kazandı")
        text = "Tahminim ", tahmin, "\n Kazandın"
    var = messagebox.showinfo("Hesap Makinesi", text)



master = tk.Tk()

tk.Button(master,
          text='Taş',
          command=tas).grid(row=0,
                                    column=0,
                                    sticky=tk.W,
                                    pady=10,
                                    padx=10)
tk.Button(master,
          text='Kağıt',
          command=kagit).grid(row=0,
                                    column=1,
                                    sticky=tk.W,
                                    pady=10,
                                    padx=10)
tk.Button(master,
          text='Makas',
          command=makas).grid(row=0,
                                    column=2,
                                    sticky=tk.W,
                                    pady=10,
                                    padx=10)

master.mainloop()
