## Kegiatan 2
a = str(input("masukkan password : "))
b = ("naufal")
for x in range(2):
    if a==b:
        print("password benar")
        break
    elif a!=b:
        a = str(input("maaf, password anda salah. Silahkan masukkan kembali password : "))
else:
    print("anda salah memasukkan password 3 kali. akses anda ditolak")
    
