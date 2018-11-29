#keg 3

import shelve

a = open("L200180142", "r")
NIM = a.readline()
TL = a.readline()
nama = a.readline()
a.close()

a = shelve.open('naufal')
a['b'] = [NIM, TL, nama]
a.close()
