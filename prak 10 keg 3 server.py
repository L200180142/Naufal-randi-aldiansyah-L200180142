import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("", 50006))
s.listen(5)
print "Server sudah siap"
perintah = ''
a=0

while perintah != 'keluar':
    komm, addr = s.accept()
    while perintah != 'keluar':
        data = komm.recv(1024).lower().split("=")
        perintah = data[0]
        if perintah == 'keluar':
            s.close()
            break
        print 'Pesan:', perintah
        if len(data) == 2:
            if perintah == 'sisi':
                a = int(data[1])
                respon = "sisi dicatat"
                komm.send(respon)
            
            else:
                komm.send('pesan tidak diketahui')
        elif perintah == 'hitung':
            L = a**2
            respon = "Luas persegi dengan sisi {} adalah {}".format(a,L)
            komm.send(respon)
        else:
            komm.send('pesan tidak diketahui')
