## kegiatan 3

a = str(input("masukkan nama : "))
b = float(input("Pukul brapa sekarang : "))
c = ('pagi', 'siang', 'sore', 'malam')
if 06.00<= b <= 09.59:
    print("Selamat " + c[0] + " "+ a)
elif 10.00<= b <= 14.59:
    print("Selamat " + c[1] + " "+ a)
elif 15.00<= b <= 17.29:
    print("Selamat " + c[2] + " "+ a)
elif 17.30<= b <= 18.59:
    print("Selamat " + c[3] + " "+ a)
elif 19.00<= b <= 23.59:
    print("Selamat " + c[4] + " "+ a)
