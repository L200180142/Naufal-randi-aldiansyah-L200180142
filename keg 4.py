Python 2.7.10 (default, May 23 2015, 09:40:32) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> nama = 'Naufal Randi Aldiansyah'
>>> nim = 142
>>> tinggi = 1.72
>>> berat = 50
>>> TahunLahir = 2000
>>> aku = (TahunLahir, berat,tinggi, nim, nama)
>>> data = [TahunLahir, berat,tinggi, nim, nama]
>>> type(aku)
<type 'tuple'>
>>> #tipe yang ada di data aku adalah tuple
>>> aku[0]
2000
>>> #data ke 0 atau yang pertama adalah tahun lahir
>>> a = nim % 4; aku[a]
1.72
>>> #nilai a adalah 1.72
>>> type(aku[4])
<type 'str'>
>>> type(aku[a])
<type 'float'>
>>> #tipe yang ada di aku dan di dalam a adalah float
>>> aku[a:4]
(1.72, 142)
>>> #terbaca dalam aku adalah nilai a dan nim
>>> type(aku[4])
<type 'str'>
>>> #tipe yang ada di aku dan urutan ke 4 adalah string
>>> aku[0] = 'ok'

Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    aku[0] = 'ok'
TypeError: 'tuple' object does not support item assignment
>>> #terjadi eroor karena tuple tidak dapat diganti datanya
>>> type(data)
<type 'list'>
>>> #tipe data yang ada di atas adalah list
>>> type(data[4])
<type 'str'>
>>> #tipe yang ada di koleksi data urutan ke 4 adalah string
>>> data[4][5]
'l'
>>> #koleksi pada data urutan ke 4 dan didalamnya ke 5 adalah huruf l
>>> data[4][a:6]
'ufal'
>>> #menampilkan koleksi dari data dan tertampil adalah ufal
>>> data[0] = 'ok' ; data
['ok', 50, 1.72, 142, 'Naufal Randi Aldiansyah']
>>> #mengganti koleksi yang ada di data menjadi ok pada urutan ke 0 dan menampilkan data yang ada setelah di ubah
>>> data[-a]
142
>>> #menampilkan data yang seperti semula
>>> range(a)
[0, 1]
>>> #urutan yang ada pada nilai a adalah 0 dan 1
>>> 
