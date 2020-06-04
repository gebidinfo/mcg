import os
import sys
import random
import time
from time import sleep
os.system('clear')
def mengetik(s):
   for c in s + '\n':
       sys.stdout.write(c)
       sys.stdout.flush()
       time.sleep(random.random () * 0.4)
a ='\033[92m'
b ='\033[91m'
c ='\033[93m'
d ='\033[95m'
e ='\033[94m'
print (a+'Loading...')
sleep(0.1)
mengetik(c+'10% 30% 60% 80% 99% | 100%')
os.system('clear')
loop = 1
pil=0
os.system('clear')
while loop == 1 :

        print """                 ____
            _[]_/____\__n_
           |_____.--.__()_| Program Hitung Luas
           |    //#  \    | Code       : python2 HitungLuas.py
           |    \____/    | Instagram  : hallo_catur
           |     '--'     | Channel YT : Gebid Info"""


        print b+'\t'
        print "1) Persegi"
        print "2) Persegi Panjang"
        print "3) Segitiga"
        print "4) Lingkaran"
        print "0) Tutup"
        print ""

        print c+'\t'

        pil = input("Masukkan Pilihan Anda : ")
        if pil ==1 :
            sisi = input("Masukkan Sisi : ")
            luas = sisi * sisi
            print "Luas Persegi Adalah",sisi,"*",sisi,"=",luas,"cm"
            time.sleep(2)
            os.system('clear')
        elif pil ==2 :
              p = input("Masukkan Panjang : ")
              l = input("Masukkan Lebar : ")
              luas = p * l
              print "Luas Persegi Panjang Adalah",p,"*",l,"=",luas,"cm"
              time.sleep(2)
              os.system('clear')
        elif pil ==3 :
              a = input("Masukkan Alas : ")
              t = input("Masukkan Tinggi : ")
              luas = a * t / 2
              print "Luas Segitiga Adalah",a,"*",t,"/ 2 =",luas,"cm"
              time.sleep(2)
              os.system('clear')
        elif pil ==4 :
              j = input("Masukkan Jari-Jari : ")
              luas = j * j * 22 / 7
              print "Luas Lingkaran Adalah",j,"*",j,"*22 / 7 =",luas,"cm"
              time.sleep(2)
              os.system('clear')
        elif pil  ==0 :
              quit("Trims : Muhammad Catur Gemilang")
              os.system('clear')
        else :
              print ("Gak Ada Menunya Gan")
              time.sleep(1)
              os.system('clear')
