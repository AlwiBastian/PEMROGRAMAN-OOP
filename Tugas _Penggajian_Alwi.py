class Employee:

    def __init__(self, name, salary, grade, num_children, married):
        self.name = name
        self.salary = salary
        self.grade = grade
        self.num_children = num_children
        self.married = married

    def get_salary(self):
        # Hitung tunjangan golongan
        if self.grade == 1:
            allowance_grade = 0.05 * self.salary
        elif self.grade == 2:
            allowance_grade = 0.1 * self.salary
        elif self.grade == 3:
            allowance_grade = 0.15 * self.salary
        elif self.grade == 4:
            allowance_grade = 0.2 * self.salary
        else:
            allowance_grade = 0

        # Hitung tunjangan anak
        if self.num_children > 0:
            allowance_children = 0.02 * self.salary * self.num_children
        else:
            allowance_children = 0    

        # Hitung tunjangan istri
        if self.married:
            allowance_spouse = 0.1 * self.salary
        else:
            allowance_spouse = 0       

        # Hitung total gaji sebelum pajak
        total_salary = self.salary + allowance_grade + allowance_children + allowance_spouse  

        # Hitung pajak
        if total_salary <= 5000000:
            tax = 0.05 * total_salary
        elif total_salary <= 10000000:
            tax = 0.1 * total_salary
        else:
            tax = 0.15 * total_salary   

        # Hitung bonus
        if self.grade == 1 and self.num_children >= 1:
            bonus = 500000
        elif self.grade == 2:
            bonus = 1000000
        elif self.grade == 3:
            bonus = 1500000
        elif self.grade == 4:
            bonus = 2000000
        else:
            bonus = 0

        # Hitung total gaji setelah pajak dan bonus
        total_salary = total_salary - tax + bonus
        return total_salary


# fungsi input untuk mengambil input dari user
name = input("Masukkan Nama karyawan : ")
salary = int(input("Masukkan Gaji Pokok Karyawan : "))
grade = int(input("Masukkan Golongan Karyawan (1-4) : "))
num_children = int(input("Masukkan Jumlah Anak Karyawan : "))
married = input("Apakah Karyawan Sudah Menikah (ya/tidak) : ").lower() == 'ya'

# Buat objek Employee baru dengan input dari user
employee = Employee(name, salary, grade, num_children, married)

# Output Cetak informasi gaji karyawan
print("-----Informasi Gaji Karyawan-----")

# Output diambil dari atribut "name" dari objek "employee".
print("Nama Karyawan:", employee.name)

# Output diambil dari atribut "salary" dari objek "employee".
print("Gaji Pokok :", employee.salary)

# Output diambil Jika grade 0, maka nilai tunjangan golongan 0. Jika grade bukan 0, maka nilai tunjangan golongan dihitung dengan rumus (0.05 + grade * 0.05) dikalikan dengan gaji pokok karyawan.
print("Tunjangan Golongan :", 0 if employee.grade == 0 else employee.salary * (0.05 + employee.grade * 0.05))

# Output dihitung dengan cara mengalikan jumlah anak dengan 0.02 kali gaji pokok karyawan.
print("Tunjangan Anak :", employee.num_children * employee.salary * 0.02)

# Output diambil Jika karyawan sudah menikah, maka tunjangan istri/suami 0.1 kali gaji pokok karyawan, jika tidak maka nilai tunjangan istri/suami adalah 0
print("Tunjangan Istri/Suami :", employee.salary * 0.1 if employee.married else 0)

#Output diambil jika karyawan memiliki grade 1 dan memiliki anak lebih dari 1, maka bonus adalah 500000dan selanjutnya. Dan jika karyawan tidak memiliki grade 1, 2, 3, 4, maka bonus adalah 0.
print("Bonus :", 500000 if employee.grade == 1 and employee.num_children >= 1 else 1000000 if employee.grade == 2 else 1500000 if employee.grade == 3 else 2000000 if employee.grade == 4 else 0)

#Output dihitung menggunakan fungsi "get_salary" dari objek "employee". Fungsi ini menghitung gaji karyawan setelah dikurangi pajak dan ditambahkan bonus.
print("Gaji Bersih :", employee.get_salary())

