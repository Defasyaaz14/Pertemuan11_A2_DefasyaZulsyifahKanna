# Fungsi untuk melakukan penambahan
def tambah(a, b):
  return a + b

# Fungsi untuk melakukan pengurangan
def kurang(a, b):
  return a - b

# Fungsi untuk melakukan perkalian
def kali(a, b):
  return a * b

# Fungsi untuk melakukan pembagian
def bagi(a, b):
  return a / b

# Menu interaktif
while True:
  # Menampilkan menu
  print("Pilihan operasi:")
  print("1. Penjumlahan")
  print("2. Pengurangan")
  print("3. Perkalian")
  print("4. Pembagian")
  pilihan = input("Masukkan pilihan (1/2/3/4): ")

  # Memvalidasi input
  while pilihan not in ("1", "2", "3", "4"):
    pilihan = input("Masukkan pilihan (1/2/3/4): ")

  # Mendapatkan input angka
  angka1 = float(input("Masukkan angka pertama: "))
  angka2 = float(input("Masukkan angka kedua: "))

  # Melakukan perhitungan
  if pilihan == "1":
    print("Hasil:", tambah(angka1, angka2))
  elif pilihan == "2":
    print("Hasil:", kurang(angka1, angka2))
  elif pilihan == "3":
    print("Hasil:", kali(angka1, angka2))
  else:
    print("Hasil:", bagi(angka1, angka2))

  # Menampilkan pertanyaan untuk melanjutkan atau tidak
  lanjutkan = input("Lanjutkan? (y/n): ")
  if lanjutkan != "y":
    break
