from tkinter import *

my_app = Tk(className='Bangun Geometri')

L1 = Label(my_app, text='Bangun Geometri', font=('comic sans', 18, 'bold'))
L1.grid(row=0, column=0, sticky=W)
L2 = Label(my_app, text='Geometri adalah ilmu yang membahas tentang hubungan antaratitik, garis, sudut, bidang, dan bangun-bangun ruang.')
L2.grid(row=1, column=0, sticky=W)
L3 = Label(my_app, text='Dimensi pada Geometri dibedakan menjadi 2, yaitu Dimensi dua dan Dimensi tiga')
L3.grid(row=2, column=0, sticky=W)
L4 = Label(my_app, text='Contoh benda Geometri adalah permukaan kertas, bola, dll')
L4.grid(row=3, column=0, sticky=W)
L5 = Label(my_app, text='Bangun Geometri Persegi', font=('Calibri', 12, 'bold'))
L5.grid(row=4, column=0, sticky=W)
L6 = Label(my_app, text='Parameter :')
L6.grid(row=5, column=0, sticky=W)
e1 = Entry(my_app)
e1.place(x=80, y=117)

def luas():
    a = float(e1.get())
    hasil = a*a
    L8.config(text=hasil)
def gambar():
    canvas = Canvas(width=300, height=300)
    canvas.pack(expand=YES, fill=BOTH)
    canvas.create_rectangle(20, 20, float(e1.get()), float(e1.get()), width=10, fill='white')
    
b1 = Button(my_app, text='Hitung Luas', command=luas)
b1.grid(row=7, column=0, sticky=W)
L7 = Label(my_app, text='Luas =', font=('Calibri', 12, 'bold'))
L7.place(x=115, y=145)
L8 = Label(my_app, text='0', font=('Calibri', 12,'bold'))
L8.place(x=185, y=145)
L9 = Label(my_app, text='Gambar  =    ', font=('Calibri', 12, 'bold'))
L9.place(x=115, y=175)
L10 = Canvas(my_app, command=gambar)
L10.place(x=185, y=175)

my_app.mainloop
