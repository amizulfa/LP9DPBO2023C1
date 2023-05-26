from tkinter import *

root = Tk()
root.title("Landing Page")

def open_residen_page():
    from data_residen import details
    root.destroy()

frame = Frame(root, padx=100, pady=100)
frame.pack()

title_label = Label(frame, text="Selamat Datang di Landing Page", font=("Arial", 18))
title_label.pack(pady=20)

button = Button(frame, text="Lihat Data Residen", command=open_residen_page)
button.pack(pady=10)

root.mainloop()
