def jumlah_angka_habis_dibagi(daftar_angka, pemisah):
  """
  Menghitung jumlah total angka dalam daftar_angka yang bisa
  dibagi habis oleh angka pemisah.

  Parameter:
    daftar_angka: List angka.
    pemisah: Angka yang digunakan untuk membagi.

  Returns:
    Jumlah total angka dalam daftar_angka yang bisa dibagi 
    habis oleh angka pemisah.
  """

  jumlah = 0
  for angka in daftar_angka:
    if angka % pemisah == 0:
      jumlah += 1
  return jumlah

# List angka
daftar_angka = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Angka pemisah
pemisah = 5

# Jumlah angka yang bisa dibagi habis oleh 5
jumlah = jumlah_angka_habis_dibagi(daftar_angka, pemisah)
print(jumlah)  # Output: 2