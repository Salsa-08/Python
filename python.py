#!/usr/bin/python2
#coding=utf-8


import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,requests,mechanize
os.system,('clear')

os.system('sh tampilan.sh')
def mengetik(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
#kecepatan mengetik
        time.sleep(random.random() * 0.2)
mengetik( 'Hallo kawan-Kawan disini kita akan belajar basic python dasar\nDari 0 Semangat Yaa kalian belajarnya calon perogrammer\nSemoga kalian paham dan bisa mengaplikasikannya\nSimak baik-baik ya pembahasannya' )

os.system('clear')
os.system('sh tampilan.sh')
os.system('sh 1.sh')
def mengetik(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
#kecepatan mengetik
        time.sleep(random.random() * 0.2)
mengetik( 'Silahkan Baca Dari Bab 1 Dulu Biar Kalian Gak Pusing' )
def pilih():
	print "===================================="
	print "Pembelajaran Python"
	print "===================================="
	print "[1] Bab(1) Pengenalan Python"
	print "===================================="
	print "[2] Bab(2) Aturan Penulisan Kode"
	print "===================================="
	print "[3] Bab(3) Variabel dan Type Data"
	print "===================================="
	print "[4] quiz python"
	print "===================================="
	print "[5] quiz2 python"
	print "===================================="
	print "[0] keluar/exit"
	print "===================================="

def bab1():
	os.system('clear')
	os.system('sh bab1.sh')
	os.system('clear')
	os.system('python2 python1.py')
def bab2():
	os.system('clear')
	os.system('python2 bab2.py')
	os.system('clear')
        os.system('python2 python1.py')
def bab3():
	os.system('clear')
        os.system('python2 bab3.py')
        os.system('clear')
        os.system('python2 python1.py')
def exit():
	os.system('clear')
	os.system('exit')
def quiz():
	os.system('clear')
        os.system('python2 quiz.py')
        os.system('clear')
        os.system('python2 python1.py')
def quiz2():
        os.system('clear')
        os.system('sh quiz2.sh')
        os.system('clear')
        os.system('python2 python1.py')

os.system('clear')
os.system('sh tampilan.sh')
os.system('figlet "PYTHON"')
pilih()
pilih = input("Pilih Bab: ")
if pilih == 1:
	bab1()
elif pilih == 2:
	bab2()
elif pilih == 3:
	bab3()
elif pilih == 4:
	quiz()
elif pilih == 5:
	quiz2()
elif pilih == 0:
	exit()
else :
	print ("nomor tidak tersedia")
	print ("silahkan pilih lagi")
	os.system('clear')
	os.system('python2 python1.py')
