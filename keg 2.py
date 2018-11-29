#keg 2

berkas = open("L200180142", "w")
berkas.write("Naufal Randi Aldiansyah. ""\n")
berkas.write("Bogor, ")
berkas.write("02/27/2000. ""\n")
berkas.write("L200180142. ")
berkas.close()

berkas = open("L200180142", "r")
print berkas.readlines()
berkas.close()
