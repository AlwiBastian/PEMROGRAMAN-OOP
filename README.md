# PEMROGRAMAN-OOP
Penjelasan Program Penggajian

Program ini adalah sebuah program Python yang menghitung gaji karyawan berdasarkan faktor, seperti gaji pokok, golongan karyawan, jumlah anak, status pernikahan, pajak, dan bonus.
Pada awal program, sebuah kelas Employee didefinisikan yang memiliki lima atribut: 
1. name (name menyimpan nama karyawan)
2. salary (salary menyimpan gaji pokok karyawan)
3. grade (grade menyimpan golongan karyawan (dari 1 hingga 4))
4. num_children (um_children menyimpan jumlah anak karyawan)
5. married (married menyimpan status pernikahan karyawan)

Fungsi get_salary() dari kelas Employee digunakan untuk menghitung gaji bersih karyawan setelah dikurangi pajak dan ditambahkan bonus. 
1. Pertama program menghitung tunjangan golongan berdasarkan grade karyawan
2. kedua program menghitung tunjangan anak berdasarkan jumlah anak karyawan
3. ketiga Program juga menghitung tunjangan istri/suami berdasarkan status pernikahan karyawan
4. setelah itu, Program menghitung total gaji sebelum pajak dengan menambahkan gaji pokok, tunjangan golongan, tunjangan anak, dan tunjangan istri/suami
5. Kemudian, program menghitung pajak berdasarkan total gaji sebelum pajak
6. Selanjutnya, program menghitung bonus berdasarkan golongan karyawan dan jumlah anak
7. Akhirnya, program menghitung gaji bersih karyawan setelah dikurangi pajak dan ditambahkan bonus dengan menggunakan fungsi get_salary() dari objek Employee

Menggunakan fungsi input() untuk mengambil input dari user berupa nama karyawan, gaji pokok, golongan, jumlah anak, dan status pernikahan. Setelah menerima input dari pengguna, program akan membuat objek Employee baru dengan memanggil konstruktor kelas Employee
Setelah itu program akan mencetak atau mengoutputkan informasi gaji karyawan dengan mengakses atribut dan metode dari objek employee

Proses outputnya program menghitung gaji karyawan dengan menghitung tunjangan golongan, tunjangan anak, dan tunjangan istri/suami terlebih dahulu. Selanjutnya, program menghitung pajak berdasarkan jumlah gaji sebelum pajak dan menghitung bonus berdasarkan grade karyawan dan jumlah anak. Setelah itu, program menghitung gaji bersih karyawan dengan mengurangi pajak dari jumlah gaji setelah tunjangan dan menambahkan bonus. Akhirnya, program mengembalikan nilai gaji bersih tersebut.
