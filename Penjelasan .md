Nama	: Nadila Hidayanti

NIM	   : 160411100182

Kelas	 : Penambangan dan Pencarian WEB 

 

TUGAS 1 : Mengambil Data dari Website menggunakan Carwl BeautifulSoup



Langkah - Langkah 

1.) Download Library BeautifulSoup menggunakan cmd pada laptop masing masing.

 - Ketik 'pip install beautifulsoup4'

   --Library untuk mengambil data

2.) Download Library requests pada cmd 

- Ketik 'pip install requests'

  --Digunakan untuk meminta data yang ada pada link web.   

3.) Download Typora

​	--Digunakan untuk menulis hasil dari tugas penambangan dan pencarian web untuk di 	  	   upload di Github sesusai dengan perintah Dosen.

4.) Buka idle Python 3.4.4 

- Menuliskan syntax 

  import requests

  from bs4 import BeautifulSoup

  -- Syntax untuk menyambungkan idle python dengan library beautifulsoup

  import requests
  from bs4 import BeautifulSoup
  import sqlite3
  --untuk menyambungkan idle dengan library beautifulsoup

  src = "https://www.kaskus.co.id/channel/6/tech"
  page = requests.get(src)
  --digunakan untuk mengelink kan web ke idle

  soup = BeautifulSoup(page.content, 'html.parser')

  a = soup.find(class_='Fw(700) C(#4a4a4a) Fz(16px) Lh(20px) Mb(7px) is-compact_Fz(14px) is-compact_Lh(16px) is-compact_Mb(10px)')
  c = soup.find(class_='Mstart(7px)')
  --diisi dengan link daata yg aakan diambil

  b = a.getText()
  d = c.getText()
  --untuk mendapatkan text nya dri code html nya 

  print(b)
  print(d)
  --memanggil

  z = soup.findAll(class_='Fw(700) C(#4a4a4a) Fz(16px) Lh(20px) Mb(7px) is-compact_Fz(14px) is-compact_Lh(16px) is-compact_Mb(10px)')
  y = soup.findAll(class_='Mstart(7px)')
  --diisi dengan link data yg akan diambil secara keseluruhan

  tampung = []
  tampung2 = []
  --sebagai wadah menampung data yang sudah di ambil
      
  for i in range (len(z)):
      tampung += [z[i].getText()]
  --mendapatkan text dari html menggunakan for karena data ada banyak
      

  for j in range (len(y)):
      tampung2 += [y[j].getText()]

  --mendapatkan text dari html menggunakan for karena data ada banyak

  conn = sqlite3.connect('dbweb1.db')
  conn.execute('''CREATE TABLE if not exists ARTIKEL
           (JUDUL TEXT NOT NULL,
           KOMENTAR TEXT NOT NULL);''')
  --untuk menyambungkan ke data ke db

  for i in range (len(tampung)):
      conn.execute('INSERT INTO ARTIKEL values ("%s", "%s");' %(tampung[i], tampung2[i]))
  --memasukkan data baru ke db

  cursor = conn.execute("SELECT* from ARTIKEL")
  for row in cursor:
      print(row)
  --menampilkan data yang ada di dalam db ketika di run

Hasil RUN

![hasil run](D:\web\hasil run.JPG)