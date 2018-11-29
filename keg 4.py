#keg 4

import shelve

a = shelve.open('naufal')
print  a['b'][0]
print  a['b'][1]
print  a['b'][2]
a.close()
