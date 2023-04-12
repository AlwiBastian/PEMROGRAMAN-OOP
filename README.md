# PEMROGRAMAN-OOP
Penjelasan Program Penggajian

Program ini adalah sebuah kelas Python yang menghitung gaji karyawan berdasarkan input yang diberikan oleh pengguna. Berikut adalah penjelasan tentang bagaimana program ini bekerja:

Kelas Employee memiliki beberapa atribut yaitu name (nama karyawan), salary (gaji pokok), grade (golongan), num_children (jumlah anak), dan married (status pernikahan). Kelas ini memiliki sebuah metode get_salary() yang menghitung gaji bersih karyawan setelah dikurangi pajak dan ditambahkan bonus.

Program akan meminta input dari pengguna berupa nama karyawan, gaji pokok, golongan, jumlah anak, dan status pernikahan (ya/tidak). Input tersebut akan digunakan untuk membuat objek Employee baru.

Program akan mencetak informasi gaji karyawan berdasarkan atribut-atribut yang ada di objek Employee. Informasi yang dicetak antara lain:

1. Nama Karyawan: nama karyawan yang diambil dari atribut name objek Employee.
2. Gaji Pokok: gaji pokok karyawan yang diambil dari atribut salary objek Employee.
3. Tunjangan Golongan: tunjangan golongan karyawan yang dihitung berdasarkan rumus (0.05 + grade * 0.05) dikalikan dengan gaji pokok karyawan. Jika golongan (grade) karyawan adalah 0, maka tunjangan golongan akan menjadi 0.
4. Tunjangan Anak: tunjangan anak karyawan yang dihitung dengan mengalikan jumlah anak (num_children) dengan 0.02 kali gaji pokok karyawan.
5. Tunjangan Istri/Suami: tunjangan istri/suami karyawan yang diambil dari atribut married objek Employee. Jika karyawan sudah menikah (married = True), maka tunjangan istri/suami akan menjadi 0.1 kali gaji pokok karyawan, jika tidak maka tunjangan istri/suami akan menjadi 0.
6. Bonus: bonus karyawan yang dihitung berdasarkan golongan (grade) karyawan. Jika golongan adalah 1 dan jumlah anak (num_children) lebih dari atau sama dengan 1, maka bonus akan menjadi 500000, jika golongan adalah 2, maka bonus akan menjadi 1000000, jika golongan adalah 3, maka bonus akan menjadi 1500000, jika golongan adalah 4, maka bonus akan menjadi 2000000, dan jika golongan bukan 1, 2, 3, atau 4, maka bonus akan menjadi 0.
7.  Gaji Bersih: gaji bersih karyawan yang dihitung menggunakan metode get_salary() dari objek Employee. Metode ini menghitung gaji karyawan setelah dikurangi pajak dan ditambahkan bonus.


