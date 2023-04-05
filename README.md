# PEMROGRAMAN-OOP
Penjelasan Program Penggajian

Program ini adalah sebuah program Python yang menghitung gaji karyawan berdasarkan faktor, seperti gaji pokok, golongan karyawan, jumlah anak, status pernikahan, pajak, dan bonus.
Pada awal program, sebuah kelas Employee didefinisikan yang memiliki lima atribut: 
-name (name menyimpan nama karyawan)
-salary (salary menyimpan gaji pokok karyawan)
-grade (grade menyimpan golongan karyawan (dari 1 hingga 4))
-num_children (um_children menyimpan jumlah anak karyawan)
-married (married menyimpan status pernikahan karyawan)

Fungsi get_salary() dari kelas Employee digunakan untuk menghitung gaji bersih karyawan setelah dikurangi pajak dan ditambahkan bonus. 
-Pertama program menghitung tunjangan golongan berdasarkan grade karyawan
-kedua program menghitung tunjangan anak berdasarkan jumlah anak karyawan
-ketiga Program juga menghitung tunjangan istri/suami berdasarkan status pernikahan karyawan
-setelah itu, Program menghitung total gaji sebelum pajak dengan menambahkan gaji pokok, tunjangan golongan, tunjangan anak, dan tunjangan istri/suami
-Kemudian, program menghitung pajak berdasarkan total gaji sebelum pajak
-Selanjutnya, program menghitung bonus berdasarkan golongan karyawan dan jumlah anak
-Akhirnya, program menghitung gaji bersih karyawan setelah dikurangi pajak dan ditambahkan bonus dengan menggunakan fungsi get_salary() dari objek Employee

Membuat inputan untuk pengguna. Setelah menerima input dari pengguna, program akan membuat objek Employee baru dengan memanggil konstruktor kelas Employee
Setelah objek Employee dibuat, program akan mencetak aatau mengoutputkan informasi gaji karyawan dengan mengakses atribut dan metode dari objek employee
