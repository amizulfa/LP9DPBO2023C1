from apartemen import Apartemen
from rumah import Rumah
from indekos import Indekos
from tkinter import *
from PIL import Image, ImageTk

hunians = []
hunians.append(Apartemen("Nelly Joy", 3, 3, "kolam renang, gym, sauna", "pythonGUI/ami/source_code/assets/apartemen.jpeg"))
hunians.append(Rumah("Sekar MK", 5, 2, "9mx5m", "pythonGUI/ami/source_code/assets/rumah.jpg"))
hunians.append(Apartemen("Park Chanyeol", 1, 3, "kolam renang, gym, sauna, biiliard, lapang golf", "pythonGUI/ami/source_code/assets/apartemen2.jpg"))
hunians.append(Rumah("Satria", 3, 4, "5mx4m", "pythonGUI/ami/source_code/assets/rumah2.jpg"))
hunians.append(Indekos("Bp. Romi", "Cahya", 750000, "pythonGUI/ami/source_code/assets/indekos.jpg"))
hunians.append(Apartemen("Zulfa", 5, 5, "kolam renang, lapang bola, lapang golf, supermarket", "pythonGUI/ami/source_code/assets/apartemen3.jpeg"))
hunians.append(Indekos("Ibu. Uu", "Romlah", 650000, "pythonGUI/ami/source_code/assets/indekos2.jpeg"))
hunians.append(Rumah("Amida", 20, 25, "150mx100m", "pythonGUI/ami/source_code/assets/rumah3.jpeg"))
hunians.append(Indekos("Bp. Isur", "Layila", 500000, "pythonGUI/ami/source_code/assets/indekos3.jpeg"))

root = Tk()
root.title("Praktikum DPBO Python")

def details(index):
    top = Toplevel()
    top.title("Detail " + hunians[index].get_jenis())

    d_frame = LabelFrame(top, text="Data Residen", padx=10, pady=10)
    d_frame.pack(padx=10, pady=10)

    # Tampilkan gambar menggunakan Label
    image = Image.open(hunians[index].get_gambar())
    image = image.resize((400, 200))
    photo = ImageTk.PhotoImage(image)
    img_label = Label(d_frame, image=photo)
    img_label.image = photo
    img_label.pack()
    img_label.grid(row=1, column=0)

    d_summary = Label(d_frame, text="Summary\n" + hunians[index].get_detail() + hunians[index].get_summary() + "\n" +
                                     hunians[index].get_dokumen(), anchor="w", justify=LEFT).grid(row=0, column=0,
                                                                                                    sticky="w")

    btn = LabelFrame(top, padx=0, pady=0)
    btn.pack(padx=10, pady=10)
    b_close = Button(btn, text="Close", command=top.destroy)
    b_close.grid(row=0, column=0)
    

frame = LabelFrame(root, text="Data Seluruh Residen", padx=10, pady=10)
frame.pack(padx=10, pady=10)

opts = LabelFrame(root, padx=10, pady=10)
opts.pack(padx=10, pady=10)

b_add = Button(opts, text="Add Data", state="disabled")
b_add.grid(row=0, column=0)

b_exit = Button(opts, text="Exit", command=root.quit)
b_exit.grid(row=0, column=1)


for index, h in enumerate(hunians):
    idx = Label(frame, text=str(index + 1), width=5, borderwidth=1, relief="solid")
    idx.grid(row=index, column=0)

    type_label = Label(frame, text=h.get_jenis(), width=15, borderwidth=1, relief="solid")
    type_label.grid(row=index, column=1)

    if h.get_jenis() != "Indekos": 
        name = Label(frame, text=" " + h.get_nama_pemilik(), width=40, borderwidth=1, relief="solid", anchor="w")
        name.grid(row=index, column=2)
    else:
        name = Label(frame, text=" " + h.get_nama_penghuni(), width=40, borderwidth=1, relief="solid", anchor="w")
        name.grid(row=index, column=2)

    b_detail = Button(frame, text="Details ", command=lambda index=index: details(index))
    b_detail.grid(row=index, column=3)

root.mainloop()