import requests
from bs4 import BeautifulSoup
import sqlite3
#untuk menyambungkan idle dengan library beautifulsoup

src = "https://www.kaskus.co.id/channel/6/tech"
page = requests.get(src)
#digunakan untuk mengelink kan web ke idle
soup = BeautifulSoup(page.content, 'html.parser')

a = soup.find(class_='Fw(700) C(#4a4a4a) Fz(16px) Lh(20px) Mb(7px) is-compact_Fz(14px) is-compact_Lh(16px) is-compact_Mb(10px)')
c = soup.find(class_='Mstart(7px)')
#diisi dengan link daata yg aakan diambil

b = a.getText()
d = c.getText()
#untuk mendapatkan text nya dri code html nya 

print(b)
print(d)
#memanggil

z = soup.findAll(class_='Fw(700) C(#4a4a4a) Fz(16px) Lh(20px) Mb(7px) is-compact_Fz(14px) is-compact_Lh(16px) is-compact_Mb(10px)')
y = soup.findAll(class_='Mstart(7px)')
#diisi dengan link daata yg aakan diambil scara keseluruhan

tampung = []
tampung2 = []
#sbagai wadah menampung data yg sdh di ambil
    
for i in range (len(z)):
    tampung += [z[i].getText()]
#mendapatkan text dri html difor kan krn data ada byk
    

for j in range (len(y)):
    tampung2 += [y[j].getText()]

#mendapatkan text dri html difor kan krn data ada byk


conn = sqlite3.connect('dbweb1.db')
conn.execute('''CREATE TABLE if not exists ARTIKEL
         (JUDUL TEXT NOT NULL,
         KOMENTAR TEXT NOT NULL);''')
#untuk menyambungkan ke data ke db

for i in range (len(tampung)):
    conn.execute('INSERT INTO ARTIKEL values ("%s", "%s");' %(tampung[i], tampung2[i]))
#memasukkan data baru ke db

cursor = conn.execute("SELECT* from ARTIKEL")
for row in cursor:
    print(row)
#menampilkan data yg ada di dlm db ketika di run
