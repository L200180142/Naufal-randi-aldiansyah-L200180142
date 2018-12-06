import socket

hostname = 'localhost'
pesan = ''
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((hostname, 2001))
print "Program Komunikasi Tentang Data Diri"
while pesan.lower() != 'keluar':
    pesan = raw_input('Perintah:')
    s.send(pesan)
    if pesan.lower() != 'keluar':
        response = s.recv(1024)
        print 'Jawab : ', response
    elif pesan.lower() == 'keluar':
        respon = s.recv(1024)
        print 'Jawab : ', respon
s.close()
