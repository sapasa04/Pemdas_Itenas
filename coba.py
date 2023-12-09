import pandas as pd

data = {'Nama': ['John', 'Jane', 'Bob', 'Alice'],
        'Usia': [25, 35, 30, 28],
        'Gaji': [50000, 60000, 70000, 55000]}

df = pd.DataFrame(data)

# Pertanyaan 1:

# Gunakan loop for dan fungsi lambda untuk menghitung gaji setiap karyawan setelah diberikan peningkatan sebesar 5% dari gaji saat ini.

for index, row in df.iterrows():
     df['Gaji_setelah_peningkatan'] = df['Gaji'].apply(lambda x: x * 1.05)
# Pertanyaan 2:
# Setelah perubahan dilakukan, tampilkan DataFrame yang sudah diperbarui dan berikan ringkasan perubahan yang telah terjadi.
print("DataFrame setelah peningkatan gaji 5%:")
print(df)
print("\nRingkasan perubahan:")
print("'Gaji_setelah_peningkatan' berhasil ditambahkan .")
print("Nilai gaji setiap karyawan dihitung dengan menambahkan 5% dari gaji saat ini.")

# Pertanyaan 3:
# Gunakan loop for lagi untuk mengevaluasi karyawan yang usianya di atas 30 tahun. Jika usia karyawan di atas 30, berikan peningkatan tambahan sebesar 2% dari gaji saat ini menggunakan fungsi lambda.

for index, row in df.iterrows():
   df['Gaji_setelah_peningkatan_usia'] = df.apply(lambda row: row['Gaji_setelah_peningkatan'] * 1.02 if row['Usia'] > 30 else row['Gaji_setelah_peningkatan'], axis=1)


# Pertanyaan 4:
# Tampilkan DataFrame yang sudah diperbarui setelah peningkatan gaji tambahan dan berikan ringkasan hasilnya.

print(" DataFrame setelah peningkatan gaji tambahan untuk usia di atas 30 tahun:")
print(df)
print("\nRingkasan hasil peningkatan gaji tambahan:")
print("'Gaji_setelah_peningkatan_usia' berhasil ditambahkan .")
print("Nilai gaji karyawan di atas 30 tahun ditingkatkan sebesar 2% dari nilai gaji setelah peningkatan 5% sebelumnya.")
