#!/usr/bin/env python
# coding: utf-8

# # Latihan Soal Untuk bahasa pemograman python
# __________________________
# 
# Pada Pelatihan ini audience mengerjakan soal-soal yang ada dibawah ini untuk melatih logika berfikir dan penyesuaian sintaks.
# 
# Terdapat 14 soal (cases) yang perlu diselesaikan dalam waktu 90 menit.
# 

# ****************************
# # Latihan Structure data 
# ### Total : 4 Soal
# ---------
# ### Tugas 1 : Sorting `List`
# Diketahui sebuah list
# 
# ```
# l = [11,2,5,23,15,8,7,6,19,21,18]
# ```
# Buat sebuah program yang mencetak nilai terkecil dan nilai terbesar pada list
# 

# In[37]:


angka = [11,2,5,23,15,8,7,6,19,21,18]
angka.sort()
print(angka)


# _______________
# ### Tugas 2 : Dictionary
# 
# https://www.w3resource.com/python-exercises/string/python-data-type-string-exercise-2.php
# 
# 
# Tulis program Python untuk membuat kamus dari string. Pergi ke editor
# 
# __Catatan:__  Hitung jumlah huruf dari `string`
# 
# Contoh `string`: 'G-Incubation'
# 
# Keluaran yang diharapkan:
# ```
# {'G': 1, '-': 1, 'I': 1, 'n': 2, 'c': 1, 'u': 1, 'b': 1, 'a': 1, 't': 1, 'i': 1, 'o': 1}
# ```

# In[38]:


def char_frequency(str1):
    dict = {}
    for n in str1: #pengecekan setiap huruf
        keys = dict.keys() #keys mengetahui jumlah data yg ada di dic
        if n in keys:
            dict[n] += 1
        else:
            dict[n] = 1
    return dict

print(char_frequency("G-Incubation"))


# ______________
# ### Tugas 3 : Tuple
# https://www.w3resource.com/python-exercises/tuple/python-tuple-exercise-33.php
# 
# Tulis program Python untuk mengonversi `list` of tupel yang diberikan di ubah ke `lisf of list`il 
# 
# ##### Hasil Keluaran
# ```
# list of  tupel : [(1, 2), (2, 3), (3, 4)]
# Ubah daftar tupel tersebut menjadi daftar daftar: [[1, 2], [2, 3], [3, 4]]
# 
# Daftar tupel asli: [(1, 2), (2, 3, 5), (3, 4), (2, 3, 4, 2)]
# Ubah daftar tupel tersebut menjadi daftar daftar: [[1, 2], [2, 3, 5], [3, 4], [2, 3, 4, 2]]
# 
# ```

# In[39]:


def test(lst_tuples):
    result = [list(el) for el in lst_tuples]
    return result

lst_tuples = [(1,2), (2,3), (3,4)]
print("List of tupel: ")
print(lst_tuples)
print("Ubah daftar tupel tersebut menjadi daftar daftar: ")
print(test(lst_tuples))

lst_tuples = [(1, 2), (2, 3, 5), (3, 4), (2, 3, 4, 2)]
print("Daftar tupel asli: ")
print(lst_tuples)
print("Ubah daftar tupel tersebut menjadi daftar daftar: ")
print(test(lst_tuples))


# ---------------
# ### Tugas 4 : Sets 
# Diketahui dua buah list :
# 
# ```
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# ```
# 
# Buat program yang mencetak hanya bilangan yang ada pada kedua list tersebut, setiap bilangan dicetak hanya sekali.

# In[40]:


a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

c = list(set(a).intersection(set(b)))
c


# ___________________________
# # Latihan logika dengan python  `if-else`
# ### Total : 4 Soal
# 
# > semakin banyak contoh kasus yang kita selesaikan maka logika kita akan semakin terlatih untuk memecahkan suatu permasalahan pemrograman.
# 
# --------
# 
# ### Tugas 1 :  Cara Menukarkan Dua Variabel
# 
# ##### Skenario Kasus
# Terdapat 2 buah variabel: 'a' dan 'b'.
# 
# Keduanya memiliki masing-masing nilai awal.
# 
# Pertanyaannya adalah: bagaimana cara menukarkan isi dari kedua variabel tersebut?
# 
# #### Hasil Keluaran
# 
# ```
# [nilai awal]
# gelas_a = kopi, gelas_b = teh
# 
# [nilai akhir]
# gelas_a = teh, gelas_b = kopi
# ```
# 

# In[41]:


#Asli
gelas_a = "kopi"
gelas_b = "teh"

print("[nilai awal]")
print(f"gelas_a = {gelas_a}")
print(f"gelas_b = {gelas_b}")

#Tukar
temp = gelas_a
gelas_a = gelas_b
gelas_b = temp

print("[nilai akhir]")
print(f"gelas_a = {gelas_a}")
print(f"gelas_b = {gelas_b}")


# ---------
# 
# ###  Tugas 2 : Bilangan Ganjil/Genap
# 
# Buatlah program yang menanyakan sebuah bilangan kepada user. Program kemudian memunculkan apakah bilangan yang dimasukkan itu genap atau ganjil.
# 
# 
# __Noted__ : Untuk menerima masukkan dari user Gunakan code ini 
# 
# ``` python
# 
# a= input('Masukkan sebuah bilangan:  ')' , # dimana a merupakan varibel penerima masukan dari user
# ```
# #### Contoh Keluaran
# > Anda memasukkan bilangan 10, 10 adalah bilangan genap
# 
# 

# In[43]:


a = input("Masukkan sebuah bilangan: ")
nilai = int(a)

print(f"Anda memasukkan bilangan {nilai}")
if(nilai%2==0):
    print(f"{nilai} adalah bilangan genap")
else:
    print(f"{nilai} adalah bilangan ganjil")


# ________________
# ###  Tugas 3 : Perbandingan `String`
# 
# #### Skenario Kasus
# Buat sebuah program berupa permainan gunting batu kertas yang dapat dimainkan oleh dua orang. Kedua pemain menginput pilihan masing-masing __(gunting/batu/kertas)__, kemudian komputer melakukan perbandingan untuk melihat dan menampilkan siapa yang menang.
# 
# 
# > (catatan: untuk menyembunyikan input dari user, dapat digunakan fungsi *getpass()* dan untuk input user gunakkan fungsi *input()* )
# 

# In[46]:


player1 = input("player 1 (gunting / batu / kertas) : ")
player2 = input("player 2 (gunting / batu / kertas) : ")

if(player1 == "gunting" and player2 == "batu"):
    print("hasil:")
    print(f"player 1: {player1}, player 2: {player2}. player 2 menang")
elif(player1 == "gunting" and player2 == "kertas"):
    print("hasil:")
    print(f"player 1: {player1}, player 2: {player2}. player 1 menang")
elif(player1 == "gunting" and player2 == "gunting"):
    print("hasil:")
    print(f"player 1: {player1}, player 2: {player2}. permainan seri")
elif(player1 == "batu" and player2 == "batu"):
    print("hasil:")
    print(f"player 1: {player1}, player 2: {player2}. permainan seri")
elif(player1 == "batu" and player2 == "kertas"):
    print("hasil:")
    print(f"player 1: {player1}, player 2: {player2}. player 2 menang")
elif(player1 == "batu" and player2 == "gunting"):
    print("hasil:")
    print(f"player 1: {player1}, player 2: {player2}. player 1 menang")
elif(player1 == "kertas" and player2 == "batu"):
    print("hasil:")
    print(f"player 1: {player1}, player 2: {player2}. player 1 menang")
elif(player1 == "kertas" and player2 == "gunting"):
    print("hasil:")
    print(f"player 1: {player1}, player 2: {player2}. player 2 menang")
elif(player1 == "kertas" and player2 == "kertas"):
    print("hasil:")
    print(f"player 1: {player1}, player 2: {player2}. permainan seri")
else:
    print("input dengan benar")


# ---------
# 
# ###  Tugas 4 : Mengukur Berat Badan
# https://koding.alza.web.id/latihan-soal-percabangan/
# ##### Skenario Kasus
# BMI (Body Mass Index) adalah salah satu cara untuk menentukan apakah seseorang bertubuh gemuk, langsing, atau kurus berdasarkan hasil bagi massa tubuh (kilogram) dengan tinggi badan (meter) kuadrat.
# 
# Nilai BMI di bawah 18.5 berarti terlalu kurus, langsing/sehat pada rentang 18.5 s.d di bawah 25, 25+ tergolong gemuk.
# 
# Buatlah sebuah program yang menanyakan berapa berat badan seseoarang (dalam kg), dan berapa tingginya (dalam cm, 1m = 100 cm), kemudian hitung nilai BMInya. Setelah nilai BMI didapatkan, cetak nilai BMI dan apakah orang tersebut termasuk kurus, langsing, atau gemuk. Lihat contoh output berikut untuk lebih jelasnya.
# 
# ##### Hasil Keluaran :
# ```
# Masukkan berat badan anda (kg): 65
# Masukkan tinggi badan anda (cm): 172
# Nilai BMI anda adalah 21,9713
# Anda termasuk berbadan langsing
# ```

# In[51]:


berat = int(input("Masukkan berat badan anda (kg): "))
tinggi = int(input("Masukkan tinggi badan anda (cm): "))/100

bmi = 0

def hitungBMI(bb, tb):
    bmi = bb/(tb**2)
    if(bmi < 18.5):
        print("Anda terlalu kurus")
    elif(bmi >= 25):
        print("Anda terlalu gemuk")
    else:
        print("Anda termasuk berbadan sehat")
    print(f"Nilai BMI anda adalah {round(bmi, 4)}")
        
hitungBMI(berat, tinggi)


#  __________________________
# # Latihan Perulangan 
# 
# ### Total : 5 Soal
# ------------
# 
# ### Tugas 1 : Mencari Nilai Maksimum dan Minimum dengan Perulangan (For dan Rekursif) 
# 
# https://replit.com/@Aswian_EditriEd/Percabangan-if-elif-else-Body-Mass-Index
# 
# ##### Skenario kasus : 
# mencari nilai terbesar, terkecil, dan nilai tengah dari 3 buah angka solusinya bisa hanya menggunakan percabangan if-else saja.
# 
# Tapi, bagaimana jika angkanya ada 7? Atau ada 8? Atau 100?
# 
# Tidak mungkin membuat percabangan if-else sebanyak itu. Oleh karena itu, kita akan mencari solusi lain yang lebih dinamis.
# 
# Buatlah program untuk memilih nilai terbasar dan terkecil dari `list` menggunakan 2 cara :
# 1. min(), max()
# 2. menggunakan perulangan for atau rekursif
# 
# ##### Hasil Keluaran :
# ```
# [3, 20, 100, -35, 50]
# Nilai terbesar: 100
# Nilai terkecil: -35
# ```
# 

# In[52]:


x = [3, 20, 100, -35, 50]
print(f"Nilai terbesar: {min(x)}")
print(f"Nilai terbesar: {max(x)}")


# ### Tugas 2 : Menghapus Nilai list sampai kosong
# 
# https://www.w3resource.com/python-exercises/basic/python-basic-1-exercise-3.php
# 
# Tulis program Python untuk menghapus dan mencetak setiap angka ketiga dari `list` angka hingga daftar menjadi kosong.
# 
# __Contoh masukan__ : [10,20,30,40,50,60,70,80,90]]
# ##### Hasil Keluaran
# ```
# 
# 30
# 60
# 90
# 40
# 80
# 50
# 20
# 70
# 10
# 
# ```

# In[53]:


list_angka = [10,20,30,40,50,60,70,80,90]

def remove_angka(list_angka):
    position = 3 - 1
    idx = 0
    len_list = (len(list_angka))
    while len_list>0:
        idx = (position+idx)%len_list
        print(list_angka.pop(idx))
        len_list -= 1

print("Data yang dihapus:")
remove_angka(list_angka)

print("Isi list_angka setelah penghapusan:")
print(list_angka)


# -----------
# 
# ### Tugas 3 : Program Bintang 1
# 
# https://codesaya.com/a/tutorial-membuat-segitiga-dengan-python-versi-bintang-mxzpdhnhux/
# 
# Tulis program Python untuk membuat pola berikut, menggunakan loop for bersarang.
# 
#          * 
#          *  * 
#          *  *  * 
#          *  *  *  * 
#          *  *  *  *  * 
#          *  *  *  *  *  * 
#          *  *  *  *  *  *  * 
#          *  *  *  *  *  *  *  * 
#          *  *  *  *  *  *  *  *  * 
#          *  *  *  *  *  *  *  *  *  * 
# 

# In[54]:


string = ""
i = 1
x = 10

while i <= x:
    j = i
    while j > 0:
        string = string + " * "
        j = j - 1
    string = string + "\n"
    i = i + 1

print(string)


#  ----------
# ### Tugas 4 : Program Bintang 2
# 
# https://codesaya.com/a/tutorial-membuat-segitiga-dengan-python-versi-bintang-mxzpdhnhux/
# 
# Tulis program Python untuk membuat pola berikut, menggunakan loop for bersarang.
# 
# 
# ```
# 
#  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  * 
# 
#     *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  * 
# 
#        *  *  *  *  *  *  *  *  *  *  *  *  *  *  * 
# 
#           *  *  *  *  *  *  *  *  *  *  *  *  * 
# 
#              *  *  *  *  *  *  *  *  *  *  * 
# 
#                 *  *  *  *  *  *  *  *  * 
# 
#                    *  *  *  *  *  *  * 
# 
#                       *  *  *  *  * 
# 
#                          *  *  * 
# 
#                             * 
# ```
# 

# In[55]:


string = ""
i = 1
x = 10

print ("\n")
# Looping Baris
while i <= x:
    j = i
    # Looping Kolom Spasi Kosong
    while j > 1:
        string = string + "   "
        j = j - 1
    # Looping Kolom Bintang Sisi Kiri
    kiri = 0
    while kiri <= (x - i):
        string = string + " * "
        kiri = kiri + 1
    # Looping Kolom Bintang Sisi Kanan
    kanan = kiri
    while kanan > 1:
        string = string + " * "
        kanan = kanan - 1

    string = string + "\n\n"
    i = i + 1
print (string)


# _______________________________
# ### Tugas 5 : Program Menghitung Huruf Vokal
# https://jagongoding.com/python/latihan-logika/menghitung-huruf-vokal/#skenario-kasus
# 
# #### Skenario Kasus
# Alur programnya;
# 
# 1. Program  akan minta user untuk memasukkan sebuah teks
# 2. Kemudian program akan menampilkan jumlah huruf vokal pada teks tersebut
# 
# #### Contoh Keluaran
# ```
# Tuliskan teks; Indonesia Adalah Negeri Sejuta Pulau
# Total karakter: 36
# Total huruf vokal: 17
#   a -> 6
#   i -> 3
#   u -> 3
#   e -> 4
#   o -> 1
#  ```
#   
# 

# In[57]:


teks = input("Tuliskan teks: ").lower()
total_karakter = 0
total_huruf_vokal = 0
huruf_vokal = {
  'a': 0,
  'i': 0,
  'u': 0,
  'e': 0,
  'o': 0
}

for karakter in teks:
    if karakter in ['a', 'i', 'u', 'e',  'o']:
        huruf_vokal[karakter] += 1
        total_huruf_vokal += 1
    total_karakter += 1
        
print(f"Total karakter: {total_karakter}")
print(f"Total huruf vokal: {total_huruf_vokal}")
print(f"""  a -> {huruf_vokal['a']}
  i -> {huruf_vokal['i']}
  u -> {huruf_vokal['u']}
  e -> {huruf_vokal['e']}
  o -> {huruf_vokal['o']}\
""")

