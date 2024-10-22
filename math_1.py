import math  # Mengimpor library math untuk operasi matematika, seperti pi

luas_lingkaran = lambda r: math.pi * r * r
#lambda: Digunakan untuk membuat fungsi anonim. Dalam konteks ini, lambda membuat fungsi yang menerima satu parameter (r) dan menghitung luas lingkaran menggunakan rumus pi * r^2.
#r: Parameter dalam fungsi lambda yang mewakili jari-jari lingkaran.
#math.pi: Konstanta pi dari library math, yang bernilai sekitar 3.14159.
#luas_lingkaran: Variabel yang menyimpan fungsi lambda untuk menghitung luas lingkaran.

# Contoh penggunaannya
jari_jari = 7  #Mendefinisikan variabel jari_jari dengan nilai 7 sebagai contoh jari-jari lingkaran yang akan dihitung.
area = luas_lingkaran(jari_jari)  #Memanggil fungsi lambda dengan memasukkan nilai jari-jari, kemudian menyimpan hasil luas lingkaran dalam variabel area.
print(f"Luas lingkaran dengan jari-jari {jari_jari} adalah {area:.2f}")  #Mencetak hasil luas lingkaran dengan format dua angka di belakang koma (desimal), yaitu hasil dari perhitungan area.