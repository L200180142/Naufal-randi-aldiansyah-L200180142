import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("", 2001))
s.listen(5)
print "Server siap"
data = ''
kamus = {'nama' : "Naufal Randi Aldiansyah",
         'NIM' : "L200180142",
         'angkatan' : "2018",
         'keluar' : "siap !!"}
while data.lower() != 'keluar':
    komm, addr = s.accept()
    while data.lower() != 'keluar':
        data = komm.recv(1024)
        if data.lower() == 'keluar':
            komm.send(kamus[data])
            s.close()
            break
        print ('Perintah:'), data
        if kamus.has_key(data):
            komm.send(kamus[data])
        else:
            komm.send('Maaf, perintah tidak dimengerti')
         
